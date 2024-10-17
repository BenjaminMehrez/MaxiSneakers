from django.shortcuts import render
from a_ecart.cart import Cart
from .forms import ShippingAddressForm
from .models import ShippingAddress

# Create your views here.


def checkout(request):
    
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    form = ShippingAddressForm(instance=request.user.profile)
    
        
    # context = {
    #     'cart_products': cart_products,
    #     'quantities': quantities,
    #     'totals' : totals,
    #     'form': form,
    # }
    
    if request.user.is_authenticated:
        form = ShippingAddressForm(request.POST, instance=request.user.profile)
        return render(request, 'a_payment/payment_page.html', {
                'cart_products': cart_products,
                'quantities': quantities,
                'totals' : totals,
                'form': form,
                })
    else:
        pass

    







def payment_success(request):
    return render(request, 'a_payment/payment_success.html')