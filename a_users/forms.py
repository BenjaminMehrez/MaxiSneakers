from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone', 'country', 'city', 'zipcode']
        widgets = {
            'first_name' : forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'last_name' : forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'phone' : forms.TextInput(attrs={'placeholder': 'Numero de Telefono'}),
            'country' : forms.TextInput(attrs={'placeholder': 'Pais'}),
            'city' : forms.TextInput(attrs={'placeholder': 'Direccion'}),
            'zipcode' : forms.TextInput(attrs={'placeholder': 'Codigo Postal'}),
        }
        
        
class EmailForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email']