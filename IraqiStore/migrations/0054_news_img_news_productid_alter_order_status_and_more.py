# Generated by Django 4.0.4 on 2022-07-28 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0053_product_hidden'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='img',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='productId',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, default='new', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='status',
            field=models.CharField(blank=True, default='new', max_length=32, null=True),
        ),
    ]
