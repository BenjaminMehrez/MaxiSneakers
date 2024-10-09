from django.shortcuts import render, get_object_or_404
from .cart import Cart
from a_store.models import Product
from django.http import JsonResponse

# Create your views here.


def cart_summary(request):
    return render(request, 'a_ecart/cart_summary.html')


def cart_add(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        
        cart_quantity = cart.__len__()
            
        # response = JsonResponse({'Product Title: ': product.title })
        response = JsonResponse({'qty': cart_quantity })
        return response

def cart_delete(request):
    pass
    

def cart_update(request):
    pass


