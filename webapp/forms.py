from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


# User registration 

class UsercreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
        
#user login
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget= TextInput())
    password = forms.CharField(widget=PasswordInput())

#Create record
    
class CreateCustomerForms(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name','email','phone_number','address','city','county','post_code']
        
#Update a record

class UpdateCustomerForms(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name','email','phone_number','address','city','county','post_code']
        
