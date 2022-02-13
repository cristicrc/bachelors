from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import CreateCustomerForm
from .models import *

import bcrypt
from datetime import date

#import settings.AUTH_USER_MODEL as User

def home(request):
    return render(request, 'accounts/home.html')


def loginPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('myaccount')
        else:
            messages.info(request, 'Username or password is incorrect...')

    return render(request, 'accounts/login.html', context)

def updateCustomerInformation(request):
    user = User.objects.filter(id=request.user.id)
    customer = CustomerData.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        id_series = request.POST.get('id_series')
        id_number = request.POST.get('id_number')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        user.update(username=username, email=email, first_name=first_name, last_name=last_name)
        customer.update(id_series=id_series, id_number=id_number, address=address, phone_number=phone_number)
    return render(request, 'accounts/updatecustomerinformation.html', {'user': user[0], 'customerData': customer[0]})

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    form = CreateCustomerForm()
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('login')
    context = {'form':form}
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
    ibanLastDigitsCreation = len(str(defaultBankingAccount.customer_id))
    defaultBankingAccount.iban[:-ibanLastDigitsCreation]
    defaultBankingAccount.iban += defaultBankingAccount.customer_id
    defaultBankingAccount.save()

def createDefaultCard():
    defaultCard = Card(
        banking_account_id=''
    )

def bankingAccount(request, bankingUrlId):
    try:
        bankingAccount = BankingAccount.objects.get(id=bankingUrlId)
        cards = Card.objects.filter(banking_account=bankingUrlId)
        transactions = Transaction.objects.filter(banking_account=bankingUrlId)
        return render(request, 'accounts/bankingAccount.html', {'bankingAccount': bankingAccount, 'cards': cards, 'transactions': transactions})
    except:
        return render(request, 'accounts/bankingAccount.html', {'message': 'Banking account does not exist...'})

def card(request, cardId):
    try:
        card = Card.objects.get(id=cardId)
        return render(request, 'accounts/cardDetails.html', {'card': card})
    except:
        return render(request, 'accounts/cardDetails.html', {'message': 'Card does not exist...'})

def transaction(request, transactionId):
    try:
        transaction = Transaction.objects.get(id=transactionId)
        return render(request, 'accounts/transactionDetails.html', {'transaction': transaction})
    except:
        return render(request, 'accounts/transactionDetails.html', {'message': 'Transaction does not exist...'})

@login_required(login_url='login')
def myAccount(request):
    bankingAccounts = BankingAccount.objects.filter(user=request.user.id)
    user = User.objects.get(id=request.user.id)
    context = {'user': user, 'bankingAccounts': bankingAccounts}
    print(context)
    return render(request, 'accounts/myaccount.html', context)

# here are some old things. use them wisely
'''
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
'''