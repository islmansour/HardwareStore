# Generated by Django 4.0.4 on 2022-05-23 18:10

import IraqiStore.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0021_rename_accountnumber_account_account_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(blank=True, default=IraqiStore.models.getuuid, max_length=12, null=True),
        ),
    ]