from ast import Del
import logging
import io
import json
from pathlib import Path
from django.core.files import File
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from IraqiStore.models import Notification, LOV, Account, AccountContacts, Contact, Delivery, Inventory, LegalDocument, News, NotificationRecipient, Order, OrderItem, Product, Quote, QutoeItem, User
from .serializers import AccountContactSerializer, FileSerializer, accountSerializer, contactSerializer, deliverySerializer, inventorySerializer, legalDocSerializer, lovSerializer, newsSerializer, notificationRecipientSerializer, notificationsSerializer, orderItemSerializer, orderSerializer, productSerializer, quoteItemSerializer, quoteSerializer, userSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate('pdfs/serviceAccountKey.json')

firebase_admin.initialize_app(cred)


class FileUploadViewSet(viewsets.ViewSet):

    def create(self, request):

        serializer_class = FileSerializer(data=request.data)
        if 'file' not in request.FILES or not serializer_class.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            handle_uploaded_file(request.FILES['file'])
            return Response(status=status.HTTP_201_CREATED)


def handle_uploaded_file(f):
    with open('./pdfs/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='myapp2.log')


def iraqi_view(request):
    return HttpResponse('hello')

# Create your views here.


@ api_view(['GET'])
def get_lovs(request):
    lov = LOV.objects.all()
    serializer = lovSerializer(lov, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_legal_doc_by_account(request, pk):
    legals = LegalDocument.objects.filter(accountId=int(pk))
    serializer = legalDocSerializer(legals, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_legal_doc_by_contact(request, pk):
    legals = LegalDocument.objects.filter(contactId=int(pk))
    serializer = legalDocSerializer(legals, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = userSerializer(users, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_user_by_uid(request, pk):
    try:

        user = User.objects.filter(uid=pk)

        serializer = userSerializer(user, many=True)

        return Response(serializer.data)

    except Exception as e:
        logging.debug(e)

    return HttpResponse('error getting user', status=500)


@ api_view(['GET'])
def get_single_user(request, pk):
    try:
        user = User.objects.filter(id=int(pk))
        serializer = userSerializer(user, many=True)
        return Response(serializer.data)

    except Exception as e:
        logging.debug(e)

    return HttpResponse('error getting user', status=500)


@ api_view(['POST'])
def upsert_user(request, pk):
    recordId = int(-1)

    try:

        record = User.objects.filter(uid=pk).first()
        request.data.update({"id": record.id})

        serializer = userSerializer(instance=record, data=request.data)
        if serializer.is_valid():
            record = serializer.save()
            recordId = record.id

        try:
            user = auth.create_user(
                #  email='user@example.com',
                email_verified=False,
                phone_number='+972'+record.uid,
                password='secretPassword',
                display_name=record.uid,
                # photo_url='http://www.example.com/12345678/photo.png',
                disabled=False)
        except Exception as inst2:
            print(type(inst2))    # the exception instance
            print(inst2.args)     # arguments stored in .args
            print(inst2)

    except Exception as inst:

        try:
            serializer = userSerializer(data=request.data)

            if serializer.is_valid():
                record = serializer.save()
                recordId = record.id

            user = auth.create_user(
                #  email='user@example.com',
                email_verified=False,
                phone_number='+972'+record.uid,
                password='secretPassword',
                display_name=record.uid,
                # photo_url='http://www.example.com/12345678/photo.png',
                disabled=False)

        except Exception as inst:
            print(type(inst))    # the exception instance
            print(inst.args)     # arguments stored in .args
            print(inst)
            HttpResponse('Error while upserting a contact.')

    return HttpResponse(str(recordId))


@ api_view(['GET'])
def get_products(request):
    products = Product.objects.all().order_by('product_number')
    serializer = productSerializer(products, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_single_product(request, pk):
    products = Product.objects.filter(product_number=pk)
    serializer = productSerializer(products, many=True)
    return Response(serializer.data)


@ api_view(['POST'])
def upsert_product(request, pk):
    recordId = int(-1)
    try:
        record = Product.objects.get(id=int(pk))
        serializer = productSerializer(instance=record, data=request.data)
        if serializer.is_valid():
            record = serializer.save()
            recordId = record.id
    except:     # arguments stored in .args

        try:

            serializer = productSerializer(data=request.data)
            if serializer.is_valid():
                record = serializer.save()
                recordId = record.id
                _notify = Notification.objects.create(
                    entity="product", entityId=recordId, message="new_product_added")
                nofSer = notificationsSerializer(data=_notify)
                nofSer.save()

        except Exception as inst:
            print(type(inst))    # the exception instance
            print(inst.args)     # arguments stored in .args
            print(inst)
            HttpResponse('Error while upserting a product.')

    return HttpResponse(str(recordId))


@ api_view(['GET'])
def get_inventory(request):
    inventory = Inventory.objects.all()
    serializer = inventorySerializer(inventory, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_single_inventory(request, pk):
    inventory = Inventory.objects.get(id=pk)
    serializer = inventorySerializer(inventory, many=False)
    return Response(serializer.data)


@ api_view(['POST'])
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


@ api_view(['GET'])
def get_contacts(request):
    contacts = Contact.objects.all()
    serializer = contactSerializer(contacts, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_single_contact(request, pk):
    contacts = Contact.objects.filter(id=int(pk))
    serializer = contactSerializer(contacts, many=True)
    return Response(serializer.data)


@ api_view(['POST'])
def upsert_contact(request, pk):
    recordId = int(-1)
    try:
        record = Contact.objects.get(id=pk)
        serializer = contactSerializer(instance=record, data=request.data)
        if serializer.is_valid():
            record = serializer.save()
            recordId = record.id
    except:
        try:
            serializer = contactSerializer(data=request.data)
            if serializer.is_valid():
                record = serializer.save()
                recordId = record.id
        except:
            HttpResponse('Error while upserting a contact.')

    return HttpResponse(str(recordId))


@ api_view(['GET'])
def get_accounts(request):
    accounts = Account.objects.all().order_by('name')
    serializer = accountSerializer(accounts, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_accounts_by_user(request, contactId):
    accounts = Account.objects.filter(contactId=contactId).order_by('name')
    serializer = accountSerializer(accounts, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_single_account(request, pk):
    accounts = Account.objects.all(id=pk)
    serializer = accountSerializer(accounts, many=False)
    return Response(serializer.data)


@ api_view(['POST'])
def upsert_account(request, pk):
    recordId = int(-1)

    try:
        record = Account.objects.get(id=pk)
        serializer = accountSerializer(instance=record, data=request.data)
        if serializer.is_valid():
            record = serializer.save()
            recordId = record.id

    except Exception as e:
        try:
            serializer = accountSerializer(data=request.data)
            if serializer.is_valid():
                record = serializer.save()
                recordId = record.id
        except Exception as e:
            return HttpResponse('Error while upserting an account.', status=400)
    return HttpResponse(str(recordId))


@ api_view(['GET'])
def get_account_contacts(request, pk):
    results = list(AccountContacts.objects.filter(
        accountId=int(pk)).values_list('contactId', flat=True))
    relatedContacts = Contact.objects.filter(id__in=results)
    serializer = contactSerializer(relatedContacts, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_contact_accounts(request, pk):
    results = list(AccountContacts.objects.all(
    ).values_list('accountId', flat=True))
    relatedContacts = Contact.objects.filter(id__in=results)
    serializer = accountSerializer(relatedContacts, many=True)

    return Response(serializer.data)


@ api_view(['POST'])
def insert_account_contact(request):
    recordId = int(-1)
    print(request.data)
    try:
        serializer = AccountContactSerializer(data=request.data)
        if serializer.is_valid():
            record = serializer.save()
            recordId = record.id
        else:
            print(({"status": "error", "data": serializer.errors}))

    except Exception as e:
        return HttpResponse('Error while inserting an AccountContactSerializer.', status=400)
    return HttpResponse(str(recordId))


@ api_view(['POST'])
def delete_account_contact(request, accountId, contactId):
    try:
        item = AccountContacts.objects.filter(
            accountId=accountId).filter(contactId=contactId)
        item.delete()
    except:
        return HttpResponse('Error while upserting an quote item.')
    return HttpResponse('success')


@ api_view(['GET'])
def get_quotes(request):
    quotes = Quote.objects.all().order_by('quote_number')
    serializer = quoteSerializer(quotes, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_quotes_by_account(request, accountId):
    quotes = Quote.objects.filter(accountId=int(accountId))
    serializer = quoteSerializer(quotes, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_quotes_by_contact(request, contactId):
    quotes = Quote.objects.filter(contactId=int(contactId))
    serializer = quoteSerializer(quotes, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_single_quote(request, pk):
    quotes = Quote.objects.get(id=pk)
    serializer = quoteSerializer(quotes, many=False)
    return Response(serializer.data)


@ api_view(['POST'])
def upsert_quote(request, pk):
    recordId = int(-1)

    try:
        record = Quote.objects.get(id=pk)
        serializer = quoteSerializer(instance=record, data=request.data)
        if serializer.is_valid():
            record = serializer.save()
            recordId = record.id

    except Exception as e:
        try:
            serializer = quoteSerializer(data=request.data)
            if serializer.is_valid():
                record = serializer.save()
                recordId = record.id

        except Exception as e:
            logging.debug(e)
            HttpResponse('-1')

    return HttpResponse(str(recordId))


@ api_view(['GET'])
def get_quote_item(request):
    items = QutoeItem.objects.all()
    serializer = quoteItemSerializer(items, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_quote_item_by_quote(request, quoteId):
    items = QutoeItem.objects.filter(quoteId=int(quoteId))
    serializer = quoteItemSerializer(items, many=True)
    return Response(serializer.data)


@ api_view(['POST'])
def upsert_quote_item(request, pk):
    recordId = int(-1)

    try:
        record = QutoeItem.objects.get(id=pk)
        serializer = quoteItemSerializer(instance=record, data=request.data)
        if serializer.is_valid():
            record = serializer.save()
            recordId = record.id
    except:
        try:
            serializer = quoteItemSerializer(data=request.data)
            if serializer.is_valid():
                record = serializer.save()
                recordId = record.id

        except:
            HttpResponse('Error while upserting an order item.')

    return HttpResponse(str(recordId))


@ api_view(['POST'])
def delete_quote_item(request, pk):
    try:
        item = QutoeItem.objects.get(pk=pk)
        item.delete()
    except:
        return HttpResponse('Error while upserting an quote item.')
    return HttpResponse('success')


@ api_view(['GET'])
def get_orders(request):
    _user_id = ""
    _user_admin = False
    if 'UID' in request.headers:
        usr = User.objects.filter(uid=str(request.headers['UID']))
        Userializer = userSerializer(usr, many=True)
        for x in Userializer.data:
            _user_id = x.get('contactId')
            _user_admin = x.get('admin')

        if _user_admin == True:
            orders = Order.objects.all().order_by('-order_number')
            serializer = orderSerializer(orders, many=True)
            return Response(serializer.data)

        if _user_admin == False:
            orders = Order.objects.filter(
                contactId=_user_id).order_by('-order_number')
            serializer = orderSerializer(orders, many=True)
            return Response(serializer.data)
    else:
        return Response('{}')


@ api_view(['GET'])
def get_orders_by_account(request, accountId):
    orders = Order.objects.filter(accountId=int(accountId))
    serializer = orderSerializer(orders, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_orders_by_contact(request, contactId):
    orders = Order.objects.filter(
        contactId=int(contactId)).order_by("-created")
    serializer = orderSerializer(orders, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_single_order(request, pk):
    orders = Order.objects.filter(id=int(pk))
    serializer = orderSerializer(orders, many=True)
    return Response(serializer.data)


@ api_view(['POST'])
def upsert_order(request, pk):
    recordId = int(-1)
    try:
        record = Order.objects.get(id=pk)
        serializer = orderSerializer(instance=record, data=request.data)
        if serializer.is_valid():
            record = serializer.save()
            recordId = record.id
            contacts = Contact.objects.filter(
                id=serializer.initial_data.get('contactId'))

            _conSer = contactSerializer(contacts, many=True)
            for con in _conSer.data:
              #  if con.get('id')==record.get('contactId'):
                usr = User.objects.filter(uid=con.get('phone'))

                Userializer = userSerializer(usr, many=True)
                if serializer.initial_data.get('status') == 'loaded':
                    _msg = 'order_loaded'
                else:
                    _msg = 'order_loaded'

                for x in Userializer.data:
                    _notify = Notification.objects.create(target=x.get('id'),
                                                          entity="client", entityId=recordId, message=_msg)
                    nofSer = notificationsSerializer(data=_notify)
                    if nofSer.is_valid():
                        nofSer.save()
    except Exception as inst:

        try:
            serializer = orderSerializer(data=request.data)
            if serializer.is_valid():
                record = serializer.save()
                recordId = record.id
                # usr = User.objects.filter(uid=str(request.headers['UID']))
                usr = User.objects.all()

                Userializer = userSerializer(usr, many=True)
                for x in Userializer.data:
                    _user_admin = x.get('admin')
                    if _user_admin == True:
                        _notify = Notification.objects.create(
                            entity="admin", entityId=recordId, message="new_order_added")
                        nofSer = notificationsSerializer(data=_notify)
                        if nofSer.is_valid():
                            nofSer.save()

        except Exception as e:
            logging.debug(e)
            return HttpResponse('Error while upserting an account.', status=400)

    return HttpResponse(str(recordId))


@ api_view(['GET'])
def get_order_item(request):
    items = OrderItem.objects.all()
    serializer = orderItemSerializer(items, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_order_item_by_order(request, orderId):
    items = OrderItem.objects.filter(orderId=int(orderId))
    serializer = orderItemSerializer(items, many=True)
    return Response(serializer.data)


@ api_view(['POST'])
def delete_order_item(request, pk):
    try:
        item = OrderItem.objects.get(pk=pk)
        item.delete()
    except:
        return HttpResponse('Error while upserting an order item.')
    return HttpResponse('success')


@ api_view(['POST'])
def upsert_order_item(request, pk):
    recordId = int(-1)

    try:
        record = OrderItem.objects.get(id=pk)
        serializer = orderItemSerializer(instance=record, data=request.data)
        if serializer.is_valid():
            record = serializer.save()
            recordId = record.id
    except:
        try:
            serializer = orderItemSerializer(data=request.data)

            if serializer.is_valid():
                record = serializer.save()
                recordId = record.id

        except:
            HttpResponse('-1')

    return HttpResponse(str(recordId))


@ api_view(['GET'])
def get_news(request):
    news = News.objects.all().order_by('-created')
    serializer = newsSerializer(news, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_active_news(request):
    news = News.objects.filter(active=True)
    serializer = newsSerializer(news, many=True)

    return Response(serializer.data)


@ api_view(['GET'])
def get_single_news(request, pk):
    news = News.objects.get(id=pk)
    serializer = newsSerializer(news, many=False)
    return Response(serializer.data)


@ api_view(['POST'])
def upsert_news(request, pk):
    recordId = int(-1)

    try:
        record = News.objects.get(id=pk)
        serializer = newsSerializer(instance=record, data=request.data)
        if serializer.is_valid():
            record = serializer.save()
            recordId = record.id
    except:
        try:
            serializer = newsSerializer(data=request.data)
            if serializer.is_valid():
                record = serializer.save()
                recordId = record.id
                _notify = Notification.objects.create(
                    entity="news", entityId=recordId, message="new_news_available")
                nofSer = notificationsSerializer(data=_notify)
                nofSer.save()

        except:
            HttpResponse('-1')
    return HttpResponse(str(recordId))


@ api_view(['GET'])
def get_user_notifications(request, pk):
    items = NotificationRecipient.objects.filter(
        userId=int(pk))
    serializer = notificationRecipientSerializer(items, many=True)
    return Response(serializer.data)


@ api_view(['POST'])
def upsert_user_notification(request, pk):
    recordId = int(-1)

    try:
        record = NotificationRecipient.objects.get(id=pk)
        serializer = notificationRecipientSerializer(
            instance=record, data=request.data)
        if serializer.is_valid():
            record = serializer.save()
            recordId = record.id
    except:
        try:
            serializer = notificationRecipientSerializer(data=request.data)
            if serializer.is_valid():
                record = serializer.save()
                recordId = record.id

        except:
            HttpResponse('-1')
    return HttpResponse(str(recordId))


@ api_view(['GET'])
def get_deliverys(request):
    deliverys = Delivery.objects.all()
    serializer = deliverySerializer(deliverys, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_deliverys_by_account(request, accountId):
    deliverys = Delivery.objects.filter(accountId=int(accountId))
    serializer = deliverySerializer(deliverys, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_deliverys_by_contact(request, contactId):
    deliverys = Delivery.objects.filter(contactId=int(contactId))
    serializer = deliverySerializer(deliverys, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def get_single_delivery(request, pk):
    news = Delivery.objects.get(id=pk)
    serializer = deliverySerializer(news, many=False)
    return Response(serializer.data)


@ api_view(['POST'])
def upsert_delivery(request, pk):
    recordId = int(-1)

    try:
        record = Delivery.objects.get(id=pk)
        serializer = deliverySerializer(instance=record, data=request.data)
        if serializer.is_valid():
            record = serializer.save()
            recordId = record.id
    except:
        try:
            serializer = deliverySerializer(data=request.data)
            if serializer.is_valid():
                record = serializer.save()
                recordId = record.id

        except:
            HttpResponse('Error while upserting an delivery item.')

    return HttpResponse(str(recordId))


@ api_view(['POST'])
def upsert_legal_document(request, pk):
    recordId = int(-1)

    try:
        record = LegalDocument.objects.get(id=pk)
        serializer = legalDocSerializer(instance=record, data=request.data)
        if serializer.is_valid():
            record = serializer.save()
            recordId = record.id
    except:
        try:
            serializer = legalDocSerializer(data=request.data)
            if serializer.is_valid():
                record = serializer.save()
                recordId = record.id

        except:
            HttpResponse('Error while upserting an order item.')

    return HttpResponse(str(recordId))


@ api_view(['GET'])
def getPDF(request, file):
    path = Path('./pdfs/'+file)

    with path.open(mode='rb') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = file
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(
            filename)

        return response
