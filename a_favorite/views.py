from django.shortcuts import render, get_object_or_404
from .favorite import Favorite
from a_store.models import *
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.


def favorite_summary(request):
    
    favorite = Favorite(request)
    favorite_products = favorite.get_prods

    return render(request, 'a_favorite/favorite_summary.html', {'favorite_products': favorite_products})


def favorite_add(request):
    
    favorite = Favorite(request)
    
    if request.POST.get('action') == 'post':
        product_id = str(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        
        favorite.add(product=product)
        
        response = JsonResponse({'product': product_id})
        messages.success(request, 'Producto agregado a favoritos')
        return response
        
        
def favorite_delete(request):
    
    favorite = Favorite(request)
    
    try:
        if request.POST.get('action') == 'post':
            product_id = str(request.POST.get('product_id'))
            favorite.delete(product=product_id)
            response = JsonResponse({'product': product_id})
            messages.success(request, 'Producto Eliminado de favoritos')
            return response
    except:
        return messages.warning(request, 'Error al eliminar producto')

