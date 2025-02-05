"""oddup_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from customers.views import CustomerViewSet, CustomerBalanceView, TransactionCreateView


customer_router = routers.SimpleRouter()
customer_router.register(r'customers', CustomerViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(customer_router.urls)),
    path('api/customers/<int:id>/account_balance/', CustomerBalanceView.as_view()),
    path('api/transactions/create/', TransactionCreateView.as_view())
]
