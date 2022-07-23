from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):
    
    username = forms.CharField(label='Usuario' ,max_length=30)
    email = forms.EmailField()
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeti la contraseña', widget=forms.PasswordInput )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        help_text = { key: '' for key in fields }