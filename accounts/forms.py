from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateCustomerForm(forms.Form):
    class Meta():
        model = Customer
        fields = ['CNP', 'email', 'password', 'password_confirmation']

class LoginCustomerForm(forms.Form):
    class Meta():
        model = Customer
        fields = ['CNP', 'password']
        CNP = forms.CharField(label='CNP', max_length=13)

class CreateCustomerDataForm(forms.Form):
    class Meta():
        model = Customer
        fields = ['customer_id', 'address', 'birthday', 'first_name','last_name', 'id_series', 'id_number', 'phone_number']
        
