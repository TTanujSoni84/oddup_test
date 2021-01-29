from rest_framework.serializers import ModelSerializer
from .models import Customer, Transaction

class CustomerSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class TransactionSerializer(ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'


class CustomerBalanceSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = ('account_balance',)