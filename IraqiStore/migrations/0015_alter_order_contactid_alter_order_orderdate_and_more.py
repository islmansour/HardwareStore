# Generated by Django 4.0.4 on 2022-05-17 20:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0014_alter_delivery_accountid_alter_delivery_contactid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='contactId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='IraqiStore.contact'),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderDate',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='quoteId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='IraqiStore.quote'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
    ]