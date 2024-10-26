from django.db import models
from django.contrib.auth.models import User
import uuid
from django.conf import settings

if settings.ENVIRONMENT == 'production':
    from cloudinary.models import CloudinaryField

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=150)
    if settings.ENVIRONMENT == 'production':
        image = CloudinaryField(null=True, blank=True)
    else:
        image = models.ImageField(upload_to='image/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=1000, decimal_places=0)
    stock = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    tags = models.ForeignKey('Tag', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['-created']
    
    def get_absolute_url(self):
        return f'/product/{self.id}'
    
        
class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)
    order = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']
        
    def get_absolute_url(self):
        return f'/category/{self.slug}'
    
