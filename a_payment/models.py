from django.db import models
from django.contrib.auth.models import User
from a_store.models import Product


# Create your models here.


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shipping_full_name = models.CharField(max_length=20)
    shipping_email = models.EmailField(max_length=40)
    shipping_address1 = models.CharField(max_length=255)
    shipping_address2 = models.CharField(max_length=255, blank=True, null=True)  # Opcional
    shipping_state = models.CharField(max_length=100)
    shipping_zipcode = models.CharField(max_length=20)
    shipping_country = models.CharField(max_length=100)
    
    
    def __str__(self):
        return f'Shipping Address - {str(self.id)}'
    
    class Meta:
        verbose_name_plural = "Shipping Address"
        
        
        
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    shipping_address = models.TextField(max_length=500)
    amount_paid = models.DecimalField(max_digits=100, decimal_places=0)
    date_ordered = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Order - {str(self.id)}'
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=100, decimal_places=0)
    
    
    def __str__(self):
        return f'Order Item - {str(self.id)}'