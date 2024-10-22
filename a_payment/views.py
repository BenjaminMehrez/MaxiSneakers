from django.shortcuts import render, redirect
from a_ecart.cart import Cart
from django.contrib import messages
from .forms import ShippingAddressForm, PaymentForm
from django.contrib.auth.models import User
from .models import *
from a_users.models import Profile


# Create your views here.


def process_order(request):
	if request.POST:
		# Get the cart
		cart = Cart(request)
		cart_products = cart.get_prods
		quantities = cart.get_quants
		totals = cart.cart_total()

		# Get Billing Info from the last page
		payment_form = PaymentForm(request.POST or None)
		# Get Shipping Session Data
		my_shipping = request.session.get('my_shipping')

		# Gather Order Info
		full_name = my_shipping['shipping_full_name']
		email = my_shipping['shipping_email']
		# Create Shipping Address from session info
		shipping_address = f"{my_shipping['shipping_address']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_zipcode']}\n{my_shipping['shipping_country']}"
		amount_paid = totals

		# Create an Order
		if request.user.is_authenticated:
			# logged in
			user = request.user
			# Create Order
			create_order = Order(user=user, full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
			create_order.save()

			# Add order items
			
			# Get the order ID
			order_id = create_order.pk
			
			# Get product Info
			for product in cart_products():
				# Get product ID
				product_id = product.id
				# Get product price
				price = product.price

				# Get quantity
				for key,value in quantities().items():
					if key == product.id:
						# Create order item
						create_order_item = OrderItem(order_id=order_id, product_id=product_id, user=user, quantity=value, price=price)
						create_order_item.save()

			# Delete our cart
			for key in list(request.session.keys()):
				if key == "session_key":
					# Delete the key
					del request.session[key]

			# Delete Cart from Database (old_cart field)
			current_user = Profile.objects.filter(user__id=request.user.id)
			# Delete shopping cart in database (old_cart field)
			current_user.update(old_cart="")


			messages.success(request, "Order Placed!")
			return redirect('home')

			

		else:
			# not logged in
			# Create Order
			create_order = Order(full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
			create_order.save()

			# Add order items
			
			# Get the order ID
			order_id = create_order.pk
			
			# Get product Info
			for product in cart_products():
				# Get product ID
				product_id = product.id
				# Get product price

				price = product.price

				# Get quantity
				for key,value in quantities().items():
					if key == product.id:
						# Create order item
						create_order_item = OrderItem(order_id=order_id, product_id=product_id, quantity=value, price=price)
						create_order_item.save()

			# Delete our cart
			for key in list(request.session.keys()):
				if key == "session_key":
					# Delete the key
					del request.session[key]



			messages.success(request, "Order Placed!")
			return redirect('home')


	else:
		messages.success(request, "Access Denied")
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
