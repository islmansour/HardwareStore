# Generated by Django 4.0.4 on 2022-06-15 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0042_account_type_alter_accountcontacts_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deliveryId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IraqiStore.delivery'),
        ),
    ]
