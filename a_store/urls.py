from django.urls import path
from .views import *


urlpatterns = [
    path('', home_view, name='home'),
    path('search/', search_products, name='search-products'),
    path('category/<tag>/', home_view, name='category'),
    path('product/create/', product_create_view, name='product-create'),
    path('product/edit/<pk>', product_edit_view, name='product-edit'),
    path('product/delete/<pk>', product_delete_view, name='product-delete'),
    path('product/<pk>/', product_page, name='product-detail'),
    # path('cart/', cart_detail, name='cart-page'),
    # path('cart/add/<product_id>/', cart_add, name='cart-add'),
    # path('cart/remove/<product_id>/', cart_remove, name='cart-remove'),   
]