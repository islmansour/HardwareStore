# Generated by Django 4.0.4 on 2022-05-27 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0027_remove_account_contact_id_contact_accountid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='orderId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderItems', to='IraqiStore.order'),
        ),
    ]
