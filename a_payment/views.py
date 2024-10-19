from django.shortcuts import render, redirect
from a_ecart.cart import Cart
from django.contrib import messages
from django.http import HttpResponse
from .forms import ShippingAddressForm
from .models import ShippingAddress

# Create your views here.


def billing_info(request):

    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()
        form = request.POST

        context = {
            'cart_products': cart_products,
            'quantities': quantities,
            'totals': totals,
            'form': form, 
        }
        return render(request, 'a_payment/payment_page_billing_info.html', context)
    else:
        messages.info(request, 'Acceco Denegado')
        return redirect('home')
        
        
        

def checkout(request):

    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()

    if request.user.is_authenticated:

        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        form = ShippingAddressForm(request.POST or None, instance=shipping_user)
        return render(request, 'a_payment/payment_page.html', {'cart_products': cart_products,
                                                               'quantities': quantities,
                                                               'totals': totals,
                                                               'form': form, })
    else:
        form = ShippingAddressForm(request.POST or None)
        return render(request, 'a_payment/payment_page.html', {'cart_products': cart_products,
                                                               'quantities': quantities,
                                                               'totals': totals,
                                                               'form': form, })


def payment_success(request):
    return render(request, 'a_payment/payment_success.html')
