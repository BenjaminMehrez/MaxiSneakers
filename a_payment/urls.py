from django.urls import path
from .views import *


urlpatterns = [
    path('payment_success/', payment_success, name='payment-success'),
    path('checkout/', checkout, name='payment-checkout'),
    path('billing_info/', billing_info, name='billing-info'),
    path('process_order/', process_order, name='process-order'),
    path('shipped_dash/', shipped_dash, name='shipped-dash'),
    path('not_shipped_dash/', not_shipped_dash, name='not-shipped-dash'),
    path('orders/<int:pk>/', orders, name='orders'),

]