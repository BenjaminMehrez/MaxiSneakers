from django.forms import ModelForm
from django import forms
from .models import *



class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'image', 'description', 'price', 'stock', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Agrega Titulo ...','id': 'product-title'}),
            'image': forms.FileInput(attrs={'class': 'hidden', 'id': 'file-upload'}),
            'description': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Agrega descripcion ...','id': 'product-description'}),
            'price': forms.NumberInput(attrs={'step': 0.01, 'min': '0', 'placeholder': 'Agrega precio  ...','id': 'product-price'}),
            'stock': forms.NumberInput(attrs={'min': '0','id': 'product-stock'}),
            'tags': forms.RadioSelect(attrs={'class': 'flex gap-4 mt-3 form-radio h-6 w-6 text-black','id': 'product-tags'}),
        }  
        
        
        
        
class ProductEditForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'image', 'description', 'price', 'stock', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Agrega Titulo ...','id': 'product-title'}),
            'image': forms.FileInput(attrs={'class': 'hidden', 'id': 'file-upload'}),
            'description': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Agrega descripcion ...','id': 'product-description'}),
            'price': forms.NumberInput(attrs={'step': 0.01, 'min': '0', 'placeholder': 'Agrega precio  ...','id': 'product-price'}),
            'stock': forms.NumberInput(attrs={'min': '0','id': 'product-stock'}),
            'tags': forms.RadioSelect(attrs={'class': 'flex gap-4 mt-3 form-radio h-6 w-6 text-black','id': 'product-tags'}),
        }   