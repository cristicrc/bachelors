from django.contrib import admin
from django.urls import path
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
    path('updatecustomerinformation/', views.updateCustomerInformation, name='updatecustomerinformation')
]
