# Generated by Django 4.0.4 on 2022-06-15 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0046_alter_order_orderdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery',
        ),
    ]