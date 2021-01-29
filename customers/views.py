from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView

from .models import Customer

from .serializers import CustomerSerializer, TransactionSerializer, CustomerBalanceSerializer


# Create your views here.

class CustomerViewSet(ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerBalanceView(RetrieveAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerBalanceSerializer
    lookup_field = 'id'

