# Generated by Django 4.0.4 on 2022-05-31 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0028_alter_orderitem_orderid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='accountId',
        ),
        migrations.AddField(
            model_name='account',
            name='contactId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IraqiStore.contact'),
        ),
        migrations.AlterField(
            model_name='qutoeitem',
            name='quoteId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quoteItems', to='IraqiStore.quote'),
        ),
    ]
