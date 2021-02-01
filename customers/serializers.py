from rest_framework.serializers import ModelSerializer
from .models import Customer, Transaction


class CustomerSerializer(ModelSerializer):
    """
    Serializer to work with customer's CRUD operations
    """

    class Meta:
        model = Customer
        fields = '__all__'


class TransactionSerializer(ModelSerializer):
    """
    Serializer to work with transaction's CRUD operations
    """

    class Meta:
        model = Transaction
        fields = '__all__'


class CustomerBalanceSerializer(ModelSerializer):
    """
    Serializer to exclusively display a customer's balance
    """

    class Meta:
        model = Customer
        fields = ('account_balance',)
