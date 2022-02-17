from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('createcustomerdata/', views.createCustomerDataPage, name='createcustomerdata'),
    path('myaccount/', views.myAccount, name='myaccount'),
    path('bankingAccount/<int:bankingUrlId>', views.bankingAccount, name='bankingAccount'),
    path('card/<int:cardId>', views.card, name='card'),
    path('transaction/<int:transactionId>', views.transaction, name='transaction'),
    path('card/create', views.cardCreate, name='cardCreate'),
    path('transaction/create', views.createTransaction, name='createTransaction'),
    path('banking-account/create', views.bankingAccountCreate, name='bankingAccountCreate'),
    path('card/delete/<int:bankingAccountId>/<int:cardId>', views.deleteCard, name='deleteCard'),
    path('updatecustomerinformation/', views.updateCustomerInformation, name='updatecustomerinformation')
]
