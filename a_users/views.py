from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from allauth.account.utils import send_email_confirmation
from django.contrib.auth.decorators import login_required
from allauth.account.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.models import User
from a_ecart.cart import Cart
from django.contrib.auth.views import redirect_to_login
from django.contrib import messages
from a_store.models import *
from .forms import *
from a_payment.forms import ShippingAddressForm
from a_payment.models import ShippingAddress
import json


# Create your views here.



class CustomLoginView(LoginView):
    
    def form_valid(self, form):
        
        response = super().form_valid(form)
        current_user = Profile.objects.get(user__id=self.request.user.id)
        saved_cart = current_user.old_cart
        if saved_cart:
            converted_cart = json.loads(saved_cart)
            cart = Cart(self.request)  

            for key, value in converted_cart.items():
                try:
                    product = Product.objects.get(id=key) 
                    cart.add(product=product, quantity=value)
                except Product.DoesNotExist:

                    print(f"Producto con id {key} no existe")

        return response




def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            return redirect_to_login(request.get_full_path())
        
    categories = Tag.objects.all()
    
    context = {
        'categories': categories,
        'profile': profile
    }
        
    return render(request, 'a_users/profile.html', context)
    
    
@login_required
def profile_edit_view(request):
    current_user = Profile.objects.get(user__id=request.user.id)
    shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
    
    form = ProfileForm(instance=current_user)
    shipping_form = ShippingAddressForm(instance=shipping_user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=current_user)
        shipping_form = ShippingAddressForm(request.POST, instance=shipping_user)
        if form.is_valid() or shipping_form.is_valid():
            form.save()
            shipping_form.save()
            
            if request.user.emailaddress_set.get(primary=True).verified:
                return redirect('profile')
            else:
                return redirect('home')
                
        
    if request.path == reverse('profile-onboarding'):
        template = 'a_users/profile_onboarding.html'
    else:
        template = 'a_users/profile_edit.html'
        
        
    categories = Tag.objects.all()
    
    context = {
        'categories': categories,
        'form': form,
        'shipping_form': shipping_form,
    }
        
    return render(request, template, context)



@login_required
def profile_settings_view(request):
    categories = Tag.objects.all()
    return render(request, 'a_users/profile_settings.html', {'categories': categories})


@login_required
def profile_emailchange(request):
    
    if request.htmx:
        form = EmailForm(instance=request.user)
        return render(request, 'partials/email_form.html', {'form':form})
    
    if request.method == 'POST':
        form = EmailForm(request.POST, instance=request.user)
        
        if form.is_valid():
            
            # Check if the email already exists
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exclude(id=request.user.id).exists():
                messages.warning(request, f'{email} ya fue esta registrado.')
                return redirect('profile-settings')
            
            form.save()
            
            # Then Signal updates emailaddress and set varified to false
            
            
            # Then send confirmation email
            send_email_confirmation(request, request.user)
            
            return redirect('profile-settings')
        else:
            messages.warning(request, 'Formulario no valido')
            return redirect('profile-settings')
    
    return redirect('home')


@login_required
def profile_emailverify(request):
    send_email_confirmation(request, request.user)
    return redirect('profile-settings')



@login_required
def profile_delete_view(request):
    user = request.user
    if request.method == 'POST':
        logout(request)
        user.delete()
        messages.success(request, 'Cuenta Eliminada, que lastima')
        return redirect('home')
    
    categories = Tag.objects.all()
    
    
    return render(request, 'a_users/profile_delete.html', {'categories': categories})