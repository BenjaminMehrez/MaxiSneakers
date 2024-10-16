from django.forms import ModelForm
from django import forms
from .models import *



class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'image', 'description', 'price', 'stock', 'tags']
        labels = {
            'tags': 'Category'
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Agrega Titulo ...'}),
            'image': forms.FileInput(),
            'description': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Agrega descripcion ...'}),
            'price': forms.NumberInput(attrs={'step': 0.01, 'min': '0', 'placeholder': 'Agrega precio ...'}),
            'stock': forms.NumberInput(attrs={'min': '0'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'flex p-5 justify-start gap-10 text-xl'}),
        }
        
        
        
        
class ProductEditForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'image', 'description', 'price', 'stock', 'tags']
        labels = {
            'tags': 'Category'
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Agrega Titulo ...'}),
            'image': forms.FileInput(),
            'description': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Agrega descripcion ...'}),
            'price': forms.NumberInput(attrs={'step': 0.01, 'min': '0', 'placeholder': 'Agrega precio  ...'}),
            'stock': forms.NumberInput(attrs={'min': '0'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'flex p-5 justify-start gap-10 text-xl'}),
        }