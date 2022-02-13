from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import *




class CreateCustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


'''
class LoginCustomerForm(forms.Form):
    class Meta():
        model = Customer
        fields = ['CNP', 'password']
        #CNP = forms.CharField(label='CNP', max_length=13)

class CreateCustomerDataForm(forms.Form):
    class Meta():
        model = Customer
        fields = ['customer_id', 'address', 'birthday', 'first_name','last_name', 'id_series', 'id_number', 'phone_number']
        
'''