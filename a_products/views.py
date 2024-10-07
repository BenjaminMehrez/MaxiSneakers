from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import *
from .forms import *
# Create your views here.


def admin_required(user):
    return user.is_superuser

def home_view(request, tag=None):
    if tag:
        products = Product.objects.filter(tags__slug=tag)
        tag = get_object_or_404(Tag, slug=tag)
    else:
        products = Product.objects.all()
        
    paginator = Paginator(products, 6)
    page = int(request.GET.get('page', 1))
    
    try:
        products = paginator.page(page)
    except:
        return HttpResponse('')
        
    categories = Tag.objects.all()
        
    context = {
        'products' : products,
        'tag' : tag,
        'categories': categories,
        'page': page
    }
    
    if request.htmx:
        return render(request, 'snippets/loop_home_products.html', context)
    
    
    return render(request, 'a_products/home.html', context)


def product_page(request, pk):
    
    product = get_object_or_404(Product, id=pk)
    
    categories = Tag.objects.all()
    
    context = {
        'categories': categories,
        'product' : product
    }
    
    return render(request, 'a_products/product_page.html', context)


def search_products(request):
    query = request.GET.get('q')
    if query:
        results = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        results = Product.objects.all()
        
    categories = Tag.objects.all()
    
    context = {
        'results': results,
        'query': query,
        'categories': categories
    }

    return render(request, 'a_products/search_page.html', context)

@user_passes_test(admin_required)
def product_create_view(request):
    form = ProductCreateForm()
    
    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    categories = Tag.objects.all()
    
    context = {
        'categories': categories,
        'form': form
    }
        
    return render(request, 'a_products/product_create.html', context)
            
            
@user_passes_test(admin_required)
def product_delete_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted')
        return redirect('home')
    
    categories = Tag.objects.all()
    
    context = {
        'categories': categories,
        'product' : product
    }
    
    return render(request, 'a_products/product_delete.html', context)



@user_passes_test(admin_required)
def product_edit_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    form = ProductEditForm(instance=product)
    
    if request.method == 'POST':
        form = ProductEditForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated')
            return redirect('home')
    
    categories = Tag.objects.all()
    
    context = {
        'form': form,
        'product': product,
        'categories': categories
    }
    
    return render(request, 'a_products/product_edit.html', context)