# Generated by Django 4.0.4 on 2022-08-22 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0059_rename_recipientid_notificationrecipient_userid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationrecipient',
            name='userId',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
