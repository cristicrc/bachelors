from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('createcustomerdata/', views.createCustomerDataPage, name='createcustomerdata'),
    path('myaccount/', views.myAccount, name='myaccount')
]
