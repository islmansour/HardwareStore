# Generated by Django 4.0.4 on 2022-06-15 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0044_rename_orderdate_order_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date',
            new_name='orderDate',
        ),
    ]
