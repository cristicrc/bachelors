from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(CustomerData)
admin.site.register(BankingAccount)
admin.site.register(Card)
admin.site.register(Transaction)
