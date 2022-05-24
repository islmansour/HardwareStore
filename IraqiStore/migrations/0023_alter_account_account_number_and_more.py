# Generated by Django 4.0.4 on 2022-05-23 21:07

import IraqiStore.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0022_alter_order_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.CharField(blank=True, default=IraqiStore.models.getAccountUID, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_number',
            field=models.CharField(blank=True, default=IraqiStore.models.getProductUID, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quote_number',
            field=models.CharField(blank=True, default=IraqiStore.models.getQuoteUID, max_length=12, null=True),
        ),
    ]