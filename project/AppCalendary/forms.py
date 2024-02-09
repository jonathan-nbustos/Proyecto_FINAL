from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

class SaludoForm(forms.ModelForm):
    class Meta:
        model = models.Saludo
        fields = "__all__"


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email: ")
    last_name = forms.CharField(label="Apellido: ")
    first_name = forms.CharField(label="Nombre: ")
    imagen = forms.ImageField(label='Avatar', required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'imagen']

class ContactoForm(forms.ModelForm):

    class Meta:
        model = models.Contacto
        fields = "__all__"