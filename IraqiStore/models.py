from email.quoprimime import quote
from itertools import product
import numbers
from statistics import quantiles
from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)  # 1
    desc = models.TextField(blank=True, null=True)  # 2
    alias = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)  # 3
    created = models.DateTimeField(default=now, editable=False)  # 4
    ceeated_by = models.IntegerField(blank=True, null=True)  # 5
    img = models.URLField(blank=True, null=True)  # 6
    active = models.BooleanField(default=True)  # 7
    discount = models.FloatField(default=0, blank=True, null=True,
                                 validators=[MinValueValidator(0), MaxValueValidator(100)])
    # need to add attributes


class Inventory(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()
    created = models.DateTimeField(default=now, editable=False)  # 5
    ceeated_by = models.IntegerField(blank=True, null=True)  # 4


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
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
    ceeated_by = models.IntegerField(blank=True, null=True)


class Account(models.Model):
    name = models.CharField(max_length=255)
    contact_id = models.ForeignKey(
        Contact, on_delete=models.DO_NOTHING, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    pobox = models.IntegerField(blank=True, null=True)
    zip = models.IntegerField(blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(default=now, editable=False)
    ceeated_by = models.IntegerField(blank=True, null=True)


class Quote(models.Model):
    STATUS = (
        (('1'), ('חדשה')),
        (('2'), ('מאושרת')),
        (('3'), ('ממתינה לאישור')),
        (('4'), ('מבוטלת'))
    )

    quoteDate = models.DateField(default=now)
    accountId = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    contactId = models.ForeignKey(Contact, on_delete=models.DO_NOTHING)
    status = models.CharField(
        max_length=32,
        choices=STATUS,
        default=1,
    )
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField(default=now, editable=False)  # 5
    ceeated_by = models.IntegerField(blank=True, null=True)  # 4


class QutoeItem(models.Model):
    quoteId = models.ForeignKey(Quote, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField(default=now, editable=False)  # 5
    ceeated_by = models.IntegerField(blank=True, null=True)  # 4


class Order(models.Model):
    STATUS = (
        (('1'), ('חדשה')),
        (('2'), ('מאושרת')),
        (('3'), ('ממתינה לאישור')),
        (('4'), ('בדרך ללקוח')),
        (('5'), ('נמסר')),
        (('6'), ('מבוטלת'))
    )

    orderDate = models.DateField(default=now)
    accountId = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    contactId = models.ForeignKey(Contact, on_delete=models.DO_NOTHING)
    status = models.CharField(
        max_length=32,
        choices=STATUS,
        default='1',
    )
    street = models.CharField(max_length=255, blank=True, null=True)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    wazeLink = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    quoteId = models.ForeignKey(Quote, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(default=now, editable=False)  # 5
    ceeated_by = models.IntegerField(blank=True, null=True)  # 4


class OrderItem(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    quoteItemId = models.ForeignKey(QutoeItem, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(default=now, editable=False)  # 5
    ceeated_by = models.IntegerField(blank=True, null=True)  # 4
