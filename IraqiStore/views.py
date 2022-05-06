from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from IraqiStore.models import Account, Contact, Inventory, Order, OrderItem, Product, Quote, QutoeItem
from .serializers import accountSerializer, contactSerializer, inventorySerializer, orderItemSerializer, orderSerializer, productSerializer, quoteItemSerializer, quoteSerializer


def iraqi_view(request):
    return HttpResponse('hello')

# Create your views here.


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = productSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_single_product(request, pk):
    products = Product.objects.get(id=pk)
    serializer = productSerializer(products, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def upsert_product(request, pk):
    try:
        record = Product.objects.get(id=pk)
        serializer = productSerializer(instance=record, data=request.data)
        if serializer.is_valid():
            serializer.save()
    except:
        try:
            serializer = productSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        except:
            return('Error while upserting a product.')

    return Response(serializer.data)


@api_view(['GET'])
def get_inventory(request):
    inventory = Inventory.objects.all()
    serializer = inventorySerializer(inventory, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_single_inventory(request, pk):
    inventory = Inventory.objects.get(id=pk)
    serializer = inventorySerializer(inventory, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def upsert_inventory(request, pk):
    try:
        record = Inventory.objects.get(id=pk)
        serializer = inventorySerializer(instance=record, data=request.data)
        if serializer.is_valid():
            serializer.save()
    except:
        try:
            serializer = inventorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        except:
            return('Error while upserting a inventory.')

    return Response(serializer.data)


@api_view(['GET'])
def get_contacts(request):
    contacts = Contact.objects.all()
    serializer = contactSerializer(contacts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_single_contact(request, pk):
    contacts = Contact.objects.get(id=pk)
    serializer = contactSerializer(contacts, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def upsert_contact(request, pk):
    try:
        record = Contact.objects.get(id=pk)
        serializer = contactSerializer(instance=record, data=request.data)
        if serializer.is_valid():
            serializer.save()
    except:
        try:
            serializer = contactSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        except:
            return('Error while upserting a contact.')

    return Response(serializer.data)


@api_view(['GET'])
def get_accounts(request):
    accounts = Account.objects.all()
    serializer = accountSerializer(accounts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_single_account(request, pk):
    accounts = Account.objects.all(id=pk)
    serializer = accountSerializer(accounts, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def upsert_account(request, pk):
    try:
        record = Account.objects.get(id=pk)
        serializer = accountSerializer(instance=record, data=request.data)
        if serializer.is_valid():
            serializer.save()
    except:
        try:
            serializer = accountSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        except:
            return('Error while upserting an account.')

    return Response(serializer.data)


@api_view(['GET'])
def get_quotes(request):
    quotes = Quote.objects.all()
    serializer = quoteSerializer(quotes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_single_quote(request, pk):
    quotes = Quote.objects.get(id=pk)
    serializer = quoteSerializer(quotes, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def upsert_quote(request, pk):
    try:
        record = Quote.objects.get(id=pk)
        serializer = quoteSerializer(instance=record, data=request.data)
        if serializer.is_valid():
            serializer.save()
    except:
        try:
            serializer = quoteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        except:
            return('Error while upserting an quote.')

    return Response(serializer.data)


@api_view(['GET'])
def get_quote_item(request):
    items = QutoeItem.objects.all()
    serializer = quoteItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def upsert_quote_item(request, pk):
    try:
        record = QutoeItem.objects.get(id=pk)
        serializer = quoteItemSerializer(instance=record, data=request.data)
        if serializer.is_valid():
            serializer.save()
    except:
        try:
            serializer = quoteItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        except:
            return('Error while upserting a quote item.')

    return Response(serializer.data)


@api_view(['GET'])
def get_orders(request):
    orders = Order.objects.all()
    serializer = orderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_single_order(request, pk):
    orders = Order.objects.get(id=pk)
    serializer = orderSerializer(orders, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def upsert_order(request, pk):
    try:
        record = Order.objects.get(id=pk)
        serializer = orderSerializer(instance=record, data=request.data)
        if serializer.is_valid():
            serializer.save()
    except:
        try:
            serializer = orderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        except:
            return('Error while upserting an order.')

    return Response(serializer.data)


@api_view(['GET'])
def get_order_item(request):
    items = OrderItem.objects.all()
    serializer = orderItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def upsert_order_item(request, pk):
    try:
        record = OrderItem.objects.get(id=pk)
        serializer = orderItemSerializer(instance=record, data=request.data)
        if serializer.is_valid():
            serializer.save()
    except:
        try:
            serializer = orderItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        except:
            return('Error while upserting an order item.')

    return Response(serializer.data)
