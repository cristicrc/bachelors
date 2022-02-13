from django.db import models
from django.conf import settings

# Create your models here.

class CustomerData(models.Model):
    CNP = models.CharField(max_length=13, null=True)
    id_series = models.CharField(max_length=2, null=True)
    id_number = models.CharField(max_length=6, null=True)
    birthday = models.DateTimeField(null=True)
    address = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=10, null=True)
    # class Meta:
    #     db_table = 'customers_data'
    
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete = models.SET_NULL)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=False)

    


class BankingAccount(models.Model):
    iban = models.CharField(max_length=24, null=True)
    account_type = models.CharField(max_length=15, null=True)
    currency = models.CharField(max_length=5, null=True)
    sold = models.FloatField()
        
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete = models.SET_NULL)

    # class Meta:
    #     db_table = 'banking_accounts'


class Card(models.Model):
    card_number = models.CharField(max_length=16, null=True)
    expiration_date = models.CharField(max_length=5, null=True)
    cvv = models.CharField(max_length=3, null=True)
    card_type = models.BooleanField(default=0) # 0-fizic ; 1-virtual
    card_status = models.BooleanField(default=0) # 0-inactiv ; 1-activ
    pin = models.CharField(max_length=4, null=True)
    
    #banking_account = models.OneToManyField()
    banking_account = models.ForeignKey(BankingAccount, null=True, on_delete = models.SET_NULL)
    
    # class Meta:
    #     db_table = 'cards'

class Transaction(models.Model):
    transaction_type = models.CharField(max_length=20, null=True)
    amount = models.FloatField()
    creation_time = models.DateTimeField(auto_now_add=True)
    receiver_iban = models.CharField(max_length=24, null=True)
    receiver_name = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=10, null=True)

    card = models.ForeignKey(Card, null=True, on_delete = models.SET_NULL)

    # class Meta:
    #     db_table = 'transactions'


# class Customer(models.Model):
#     email = models.EmailField(null=True)
#     password = models.CharField(max_length=100, null=True)
    
#     created_date = models.DateTimeField(auto_now_add=True, null=True)

#     def __str__(self):
#         return self.email
    # USERNAME_FIELD = 'CNP'
    # def __str__(self):
    #    pass
    # class Meta:
    #    db_table = 'customers'