from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from IraqiStore.models import Account, Contact, Inventory, Product
from .serializers import accountSerializer, contactSerializer, inventorySerializer, productSerializer


def iraqi_view(request):
    return HttpResponse('hello')

# Create your views here.


@api_view(['GET'])
def get_data(request):
    products = Product.objects.all()
    serializer = productSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_inventory(request):
    inventory = Inventory.objects.all()
    serializer = inventorySerializer(inventory, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_contacts(request):
    contacts = Contact.objects.all()
    serializer = contactSerializer(contacts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_accounts(request):
    accounts = Account.objects.all()
    serializer = accountSerializer(accounts, many=True)
    return Response(serializer.data)
