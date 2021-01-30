from django.db import models

# Create your models here.


class Customer(models.Model):
    """
    This is the standard customer model for the scope of this test task.
    In a fully blown application, it would be ideal to subclass both the 
    AbstractUser and the BaseUserManager classes and implement a basic auth mechanism.
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    account_balance = models.FloatField(default=0.0)
    purchases = models.IntegerField(default=0)


class Transaction(models.Model):
    """
    Model to store transaction information
    """
    customer = models.ForeignKey(
        Customer, related_name='transactions', on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    item = models.CharField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)
