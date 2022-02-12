from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .forms import *
from .models import *

import bcrypt
from datetime import date


def home(request):
    return render(request, 'accounts/home.html')


def loginPage(request):
    form = LoginCustomerForm()
    context = {'form':form}
    if request.method == 'POST':
        form = LoginCustomerForm(request.POST)
        user = Customer.objects.get(CNP=form.data['CNP'])
        print('login HERE!!')
        password = form.data['password'].encode('utf-8')
        user.password = user.password[2:-1]
        user.password = user.password.encode()
        #print(str(password) + ' ' + str(type(password)))
        #print(str((user.password)) + ' '+ str(type(user.password)))
        salt = bcrypt.gensalt()
        #print(user.id)
        if bcrypt.checkpw(password, user.password):
            print(user.email)
        else:
            print("does not match")
        user = authenticate(request, CNP=user, password=password)
        print(type(user))

        #if user is not None:
        #    login(request, user)
        return redirect('home')

    #form = CreateUserForm()
    return render(request, 'accounts/login.html')#, context)

def myAccount():
    pass

def registerPage(request):
    form = CreateCustomerForm()
    context = {'form':form}
    print("start")
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.data['password'].encode('utf-8'), salt)
        hashed_password_confirmation = bcrypt.hashpw(form.data['password_confirmation'].encode('utf-8'), salt)
        if hashed_password != hashed_password_confirmation:
            raise forms.ValidationError("Passwords must be identical.")
        #print(hashed)
        if form.is_valid():
            print("form is valid")
            #print (form.data['email'])
            user = Customer(
                CNP = form.data['CNP'],
                email = form.data['email'],
                password = hashed_password
            ).save()
            #user.save()
            #print(str(user.CNP + ' '+ user.email+' '+ user.password))
            return redirect('login')

    return render(request, 'accounts/register.html', context)


def createCustomerDataPage(request):
    form = CreateCustomerDataForm(request)
    context = {'form':form}
    if request.method == 'POST':
        form = CreateCustomerDataForm(request.POST)
        if form.is_valid():
            customerData = CustomerData(
                customer_id=15,
                address=form.data['address'],
                birthday=date(year=1997, month=12, day=13),
                first_name=form.data['first_name'],
                last_name=form.data['last_name'],
                id_series=form.data['id_series'],
                id_number=form.data['id_number'],
                phone_number=form.data['phone_number']
            ).save()
    return render(request, 'accounts/createcustomerdata.html', context)

def createDefaultBankingAccount():
    defaultBankingAccount =  BankingAccount(
        account_type='Current Account',
        customer_id='15',
        iban='RO97MYBNK000000000000000',
        currency='RON',
        sold=0
    )
    ibanLastDigitsCreation = len(defaultBankingAccount.customer_id)
    defaultBankingAccount.iban[:-ibanLastDigitsCreation]
    defaultBankingAccount.iban += defaultBankingAccount.customer_id
    defaultBankingAccount.save()

def createDefaultCard():
    defaultCard = Card(
        banking_account_id=''
    )

def myAccount(request):
    return render(request, 'accounts/myaccount.html')
