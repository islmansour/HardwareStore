# Generated by Django 4.0.4 on 2022-05-12 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0010_order_delivery_quote_delivery'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, editable=False)),
                ('ceeated_by', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
