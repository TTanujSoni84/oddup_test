from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    account_balance = models.FloatField(default=0.0)
    purchases = models.IntegerField(default=0)


class Transaction(models.Model):
    customer = models.ForeignKey(
        Customer, related_name='transactions', on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    item = models.CharField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)
