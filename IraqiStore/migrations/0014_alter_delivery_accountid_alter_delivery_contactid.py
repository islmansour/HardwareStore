# Generated by Django 4.0.4 on 2022-05-15 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0013_alter_orderitem_quoteitemid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='accountId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='IraqiStore.account'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='contactId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='IraqiStore.contact'),
        ),
    ]
