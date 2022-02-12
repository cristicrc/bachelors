from django.db import models

# Create your models here.

class Customer(models.Model):
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100, null=True)
    CNP = models.CharField(max_length=13, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    USERNAME_FIELD = 'CNP'
    #def __str__(self):
    #    pass
    class Meta:
        db_table = 'customers'


class CustomerData(models.Model):
    customer_id = models.CharField(max_length=10, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    id_series = models.CharField(max_length=2, null=True)
    id_number = models.CharField(max_length=6, null=True)
    birthday = models.DateTimeField(null=True)
    address = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=10, null=True)
    class Meta:
        db_table = 'customers_data'

class BankingAccount(models.Model):
    customer_id = models.CharField(max_length=10, null=True)
    iban = models.CharField(max_length=24, null=True)
    account_type = models.CharField(max_length=15, null=True)
    currency = models.CharField(max_length=5, null=True)
    sold = models.FloatField()
    class Meta:
        db_table = 'banking_accounts'

class Card(models.Model):
    banking_account_id = models.CharField(max_length=10, null=True)
    card_number = models.CharField(max_length=16, null=True)
    expiration_date = models.CharField(max_length=5, null=True)
    cvv = models.CharField(max_length=3, null=True)
    card_type = models.BooleanField(default=0) # 0-fizic ; 1-virtual
    card_status = models.BooleanField(default=0) # 0-inactiv ; 1-activ
    pin = models.CharField(max_length=4, null=True)
    class Meta:
        db_table = 'cards'

class Transaction(models.Model):
    banking_account_id = models.CharField(max_length=10, null=True)
    transaction_type = models.CharField(max_length=20, null=True)
    amount = models.FloatField()
    creation_time = models.DateTimeField(auto_now_add=True)
    card_id = models.CharField(max_length=10, null=True)
    receiver_iban = models.CharField(max_length=24, null=True)
    receiver_name = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=10, null=True)
    class Meta:
        db_table = 'transactions'