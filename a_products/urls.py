from django.urls import path
from .views import *


urlpatterns = [
    path('', home_view, name='home'),
    path('category/<tag>/', home_view, name='category'),
    path('product/create/', product_create_view, name='product-create'),
    path('product/edit/<pk>', product_edit_view, name='product-edit'),
    path('product/delete/<pk>', product_delete_view, name='product-delete'),
    path('product/<pk>/', product_page, name='product'),
]