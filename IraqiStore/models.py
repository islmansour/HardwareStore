from ast import Or
from datetime import datetime
from email.quoprimime import quote
from itertools import product
from os import access
from pydoc import describe
from xmlrpc.client import DateTime
# import numbers
# from statistics import quantiles
from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.functions import Substr, Length


def getuuid():
    return str(200000+Order.objects.latest('id').id+1)


def getProductUID():
    return str(300000+Product.objects.latest('id').id+1)


def getAccountUID():
    return str(400000+Account.objects.latest('id').id+1)


def getQuoteUID():
    return str(500000+Quote.objects.latest('id').id+1)


def getOrderUID():
    return str(200000+Order.objects.latest('id').id+1)


class LOV(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(default=True)
    language = models.CharField(
        default='he', max_length=2, blank=True, null=True)

    class Meta:
        unique_together = ('type', 'name', 'language')

    def __str__(self) -> str:
        return self.type+"|"+self.name+"|"+self.language


class Product(models.Model):
    product_number = models.CharField(
        max_length=12, default=getProductUID, blank=True, null=True)

    name = models.CharField(max_length=255)  # 1
    desc = models.TextField(blank=True, null=True)  # 2
    alias = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)  # 3
    created = models.DateTimeField(default=now, editable=False)  # 4
    created_by = models.IntegerField(blank=True, null=True)  # 5
    img = models.CharField(max_length=2048, blank=True, null=True)  # 6
    active = models.BooleanField(default=True)  # 7
    discount = models.FloatField(default=0, blank=True, null=True,
                                 validators=[MinValueValidator(0), MaxValueValidator(100)])
    category = models.CharField(max_length=50, blank=True, null=True)
    sub_category = models.CharField(max_length=50, blank=True, null=True)
    # need to add attributes

    def __str__(self) -> str:
        return self.name


class Inventory(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(default=now, editable=False)  # 5
    created_by = models.IntegerField(blank=True, null=True)  # 4


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    accountId = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    phone2 = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    pobox = models.IntegerField(blank=True, null=True)
    zip = models.IntegerField(blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(default=now, editable=False)
    created_by = models.IntegerField(blank=True, null=True)


class Account(models.Model):
    account_number = models.CharField(
        max_length=12, default=getAccountUID, blank=True, null=True)

    name = models.CharField(max_length=255)
    contactId = models.ForeignKey(
        Contact, on_delete=models.CASCADE, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    pobox = models.IntegerField(blank=True, null=True)
    zip = models.IntegerField(blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(default=now, editable=False)
    created_by = models.IntegerField(blank=True, null=True)


class Quote(models.Model):
    quoteDate = models.DateField(default=now, blank=True, null=True)
    accountId = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    contactId = models.ForeignKey(
        Contact, on_delete=models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(
        max_length=32, blank=True, null=True)
    quote_number = models.CharField(
        max_length=12, default=getQuoteUID, blank=True, null=True)

    notes = models.TextField(blank=True, null=True)
    delivery = models.BooleanField(default=False)
    created = models.DateTimeField(default=now, editable=False)  # 5
    created_by = models.IntegerField(blank=True, null=True)  # 4


class QutoeItem(models.Model):
    quoteId = models.ForeignKey(
        Quote, related_name='quoteItems', on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)

    created = models.DateTimeField(default=now, editable=False)  # 5
    created_by = models.IntegerField(blank=True, null=True)  # 4


class Order(models.Model):
    orderDate = models.DateField(default=now, blank=True, null=True)

    accountId = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    contactId = models.ForeignKey(
        Contact, on_delete=models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(
        max_length=32, blank=True, null=True)
    order_number = models.CharField(
        max_length=12, default=getOrderUID, blank=True, null=True)

    street = models.CharField(max_length=255, blank=True, null=True)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    wazeLink = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    quoteId = models.ForeignKey(
        Quote, on_delete=models.DO_NOTHING, blank=True, null=True)
    delivery = models.BooleanField(default=False)
    created = models.DateTimeField(default=now, editable=False)  # 5
    created_by = models.IntegerField(blank=True, null=True)  # 4


class OrderItem(models.Model):
    orderId = models.ForeignKey(
        Order, related_name='orderItems', on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)

    price = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    quoteItemId = models.ForeignKey(
        QutoeItem, on_delete=models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField(default=now, editable=False)  # 5
    created_by = models.IntegerField(blank=True, null=True)  # 4


class News(models.Model):
    desc = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(default=now, editable=False)  # 5
    created_by = models.IntegerField(blank=True, null=True)


class Delivery(models.Model):
    date = models.DateTimeField()
    accountId = models.ForeignKey(
        Account, on_delete=models.DO_NOTHING, blank=True, null=True)
    contactId = models.ForeignKey(
        Contact, on_delete=models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(
        max_length=32,
    )
    wazeLink = models.CharField(max_length=255, blank=True, null=True)
    approvalLink = models.CharField(max_length=255, blank=True, null=True)


class User(models.Model):
    uid = models.CharField(max_length=256, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    login = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(default=now, editable=False)  # 5
    created_by = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.first_name
