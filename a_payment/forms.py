from django.forms import ModelForm
from django import forms
from .models import ShippingAddress


class ShippingAddressForm(ModelForm):
    
    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_address', 'shipping_street', 'shipping_zipcode', 'shipping_city', 'shipping_country']
        exclude = ['user']
        widgets = {
            'shipping_full_name': forms.TextInput(attrs={'placeholder': 'Lionel Messi'}),
            'shipping_email': forms.EmailInput(attrs={'placeholder': 'lionelmessi@gmail.com'}),
            'shipping_address': forms.Textarea(attrs={'rows': '1', 'placeholder': 'Barrio Champions, Rosario'}),
            'shipping_street': forms.TextInput(attrs={'placeholder': '9 de julio 231'}),
            'shipping_zipcode': forms.TextInput(attrs={'placeholder': '4122'}),
            'shipping_city': forms.TextInput(attrs={'placeholder': 'Santa Fe'}),
            'shipping_country': forms.TextInput(attrs={'placeholder': 'Argentina'}),
        }
        labels = {
            'shipping_full_name': 'Nombre completo',
            'shipping_email': 'Correo Electrónico',
            'shipping_address': 'Dirección',
            'shipping_street': 'Calle y número',
            'shipping_zipcode': 'Condigo Postal',
            'shipping_city': 'Provincia',
            'shipping_country': 'País',
        }
