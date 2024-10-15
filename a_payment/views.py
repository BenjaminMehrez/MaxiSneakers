from django.shortcuts import render
from a_ecart.cart import Cart


# Create your views here.


def checkout(request):
    
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    
    context = {
        'cart_products': cart_products,
        'quantities': quantities,
        'totals' : totals
    }
    
    return render(request, 'a_payment/payment_checkout.html', context)







def payment_success(request):
    return render(request, 'a_payment/payment_success.html')