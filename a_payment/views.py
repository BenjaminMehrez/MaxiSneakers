from django.shortcuts import render, redirect
from a_ecart.cart import Cart
from django.contrib import messages
from .forms import ShippingAddressForm, PaymentForm
from django.contrib.auth.models import User
from .models import *
from a_store.models import Product
# Create your views here.


def process_order(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()
        form = request.POST
        
        payment_form = PaymentForm(request.POST or None)
        my_shipping = request.session.get('my_shipping')
        
        full_name = my_shipping['shipping_full_name']
        email = my_shipping['shipping_email']
        shipping_address = f'{my_shipping['shipping_address']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_zipcode']}\n{my_shipping['shipping_country']}'
        amount_paid = totals
    
        if request.user.is_authenticated:
            user = request.user
            create_order = Order(user=user, full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
            create_order.save()
                    
            order_id = create_order.pk
            
            for product in cart_products():
                product_id = product.id        
                price = product.price
            
            for key,value in quantities().items():
                if key == product.id:
                    create_order_item = OrderItem(order_id=order_id, product_id=product_id, quantity=value, price=price)
                    create_order_item.save()
                    
                    
            messages.info(request, 'Order placed!')
            return redirect('home')
        else:
            create_order = Order(full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
            create_order.save()

            messages.info(request, 'Order placed!')
            return redirect('home')
    else:
        messages.info(request, 'Acceco Denegado')
        return redirect('home')





def billing_info(request):

    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()
        form = request.POST


        my_shipping = request.POST
        request.session['my_shipping'] = my_shipping

        if request.user.is_authenticated:
            billing_form = PaymentForm()
            return render(request, 'a_payment/payment_page_billing_info.html', {'cart_products': cart_products,
                                                                                'quantities': quantities,
                                                                                'totals': totals,
                                                                                'form': request.POST,
                                                                                'billing_form': billing_form,
                                                                                })
        else:
            billing_form = PaymentForm()
            return render(request, 'a_payment/payment_page_billing_info.html', {'cart_products': cart_products,
                                                                                'quantities': quantities,
                                                                                'totals': totals,
                                                                                'form': request.POST,
                                                                                'billing_form': billing_form,})
            
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
        form = ShippingAddressForm(
            request.POST or None, instance=shipping_user)
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
