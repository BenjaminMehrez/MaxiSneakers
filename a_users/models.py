from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
from django.conf import settings
if settings.ENVIRONMENT == 'production':
    from cloudinary.models import CloudinaryField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    if settings.ENVIRONMENT == 'production':
        image = CloudinaryField( null=True, blank=True) 
    else:
        image = models.ImageField(upload_to='avatars/', null=True, blank=True) # blank signify that can is empty, null can save something empty
    
    first_name = models.CharField(max_length=10, null=True)
    last_name = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    old_cart = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(User, auto_now_add=True)
    
    
    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.user.username
        
    
    
    @property
    def name(self):
        if self.first_name:
            return self.first_name
        return self.user.username
    
    
    @property
    def avatar(self):
        try:
            avatar = self.image.url
        except:
            avatar = static('images/avatar_default.jpg')
        return avatar