from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)  # 1
    desc = models.TextField(blank=True, null=True)  # 2
    alias = models.CharField(max_length=255)
    price = models.FloatField(null=True)  # 3
    created = models.DateTimeField(default=now, editable=False)  # 4
    ceeated_by = models.IntegerField(null=True)  # 5
    img = models.URLField(null=True)  # 6
    active = models.BooleanField(default=True)  # 7
    discount = models.FloatField(default=0,
                                 validators=[MinValueValidator(0), MaxValueValidator(100)])
    # need to add attributes
