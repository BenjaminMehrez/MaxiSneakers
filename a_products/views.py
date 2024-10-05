from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.


def home_view(request, tag=None):
    
    if tag:
        products = Product.objects.filter(tags__slug=tag)
        tag = get_object_or_404(Tag, slug=tag)
    else:
        products = Product.objects.all()
        
    categories = Tag.objects.all()
        
    context = {
        'products' : products,
        'tag' : tag,
        'categories': categories
    }
    
    return render(request, 'a_products/home.html', context)


def product_page(request, pk):
    
    product = get_object_or_404(Product, id=pk)
    
    return render(request, 'a_products/product_page.html', {'product' : product})



@login_required
def product_create_view(request):
    form = ProductCreateForm()
    
    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    return render(request, 'a_products/product_create.html', {'form': form})
            
            
@login_required
def product_delete_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted')
        return redirect('home')
    
    return render(request, 'a_products/product_delete.html', {'product' : product})



@login_required
def product_edit_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    form = ProductEditForm(instance=product)
    
    if request.method == 'POST':
        form = ProductEditForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated')
            return redirect('home')
    
    context = {
        'form': form,
        'product': product
    }
    
    return render(request, 'a_products/product_edit.html', context)