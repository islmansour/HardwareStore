# Generated by Django 4.0.4 on 2022-08-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0056_crontest'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='entity',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='entityId',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
