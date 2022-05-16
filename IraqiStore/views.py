import logging
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from IraqiStore.models import LOV, Account, Contact, Delivery, Inventory, News, Order, OrderItem, Product, Quote, QutoeItem
from .serializers import accountSerializer, contactSerializer, deliverySerializer, inventorySerializer, lovSerializer, newsSerializer, orderItemSerializer, orderSerializer, productSerializer, quoteItemSerializer, quoteSerializer

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='myapp2.log')


def iraqi_view(request):
    return HttpResponse('hello')

# Create your views here.


@api_view(['GET'])
def get_lovs(request):
    logging.debug(request)
    lov = LOV.objects.all()
    serializer = lovSerializer(lov, many=True)
    return Response(serializer.data)


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
    logging.info(pk)

    logging.debug(request)
    try:
        record = Product.objects.get(id=int(pk))
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
def get_quotes_by_account(request, accountId):
    quotes = Quote.objects.filter(accountId=int(accountId))
    serializer = quoteSerializer(quotes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_quotes_by_contact(request, contactId):
    quotes = Quote.objects.filter(contactId=int(contactId))
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


@api_view(['GET'])
def get_quote_item_by_quote(request, quoteId):
    items = QutoeItem.objects.filter(quoteId=int(quoteId))
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
def get_orders_by_account(request, accountId):
    orders = Order.objects.filter(accountId=int(accountId))
    serializer = orderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_orders_by_contact(request, contactId):
    orders = Order.objects.filter(contactId=int(contactId))
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


@api_view(['GET'])
def get_order_item_by_order(request, orderId):
    items = OrderItem.objects.filter(orderId=int(orderId))
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


@api_view(['GET'])
def get_news(request):
    news = News.objects.all()
    serializer = newsSerializer(news, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_single_news(request, pk):
    news = News.objects.get(id=pk)
    serializer = newsSerializer(news, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def upsert_news(request, pk):
    try:
        record = News.objects.get(id=pk)
        serializer = newsSerializer(instance=record, data=request.data)
        if serializer.is_valid():
            serializer.save()
    except:
        try:
            serializer = newsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        except:
            return('Error while upserting a news.')

    return Response(serializer.data)


@api_view(['GET'])
def get_deliverys(request):
    deliverys = Delivery.objects.all()
    serializer = deliverySerializer(deliverys, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_deliverys_by_account(request, accountId):
    deliverys = Delivery.objects.filter(accountId=int(accountId))
    serializer = deliverySerializer(deliverys, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_deliverys_by_contact(request, contactId):
    deliverys = Delivery.objects.filter(contactId=int(contactId))
    serializer = deliverySerializer(deliverys, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_single_delivery(request, pk):
    news = Delivery.objects.get(id=pk)
    serializer = deliverySerializer(news, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def upsert_delivery(request, pk):
    try:
        record = Delivery.objects.get(id=pk)
        serializer = deliverySerializer(instance=record, data=request.data)
        if serializer.is_valid():
            serializer.save()
    except:
        try:
            serializer = deliverySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        except:
            return('Error while upserting a Delivery.')

    return Response(serializer.data)
