from django.shortcuts import render
from django.db import transaction
from django.db.models import F

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Customer, Transaction

from .serializers import CustomerSerializer, TransactionSerializer, CustomerBalanceSerializer


class CustomerViewSet(ModelViewSet):
    """
    This viewset performs basic CRUD operations on customer
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerBalanceView(RetrieveAPIView):
    """
    View to display customer balance
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerBalanceSerializer
    lookup_field = 'id'


class TransactionCreateView(CreateAPIView):
    """
    View to create a transaction and handle customer balance
    accordingly.
    """

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    # Transaction needs to be atomic in order to roll back all the database changes
    # if one of the queries fail
    @transaction.atomic
    def create(self, request):

        serializer = self.get_serializer(data=request.data)

        # validating user data
        if serializer.is_valid():
            customer_id = request.data.get('customer')

            # This object is necessary to check the balance before deduction
            customer = Customer.objects.get(pk=customer_id)

            # check whether a customer has enough account balance to
            # make this purchase
            if customer.account_balance < request.data.get('price'):
                return Response("The customer doesn't have enough balance", status=status.HTTP_400_BAD_REQUEST)

            self.perform_create(serializer)

            # update the customer's balance post purchase
            # TODO: Add database level check to prevent negative values
            # Using update here works in tandem with @transaction.atomic in order to maintain
            # thread safety
            Customer.objects.filter(pk=customer_id).update(account_balance=F(
                'account_balance')-request.data.get('price'))

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
