# Generated by Django 4.0.4 on 2022-08-20 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0057_notification_entity_notification_entityid'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='token',
            field=models.TextField(blank=True, null=True),
        ),
    ]