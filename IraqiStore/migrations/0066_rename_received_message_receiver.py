# Generated by Django 4.0.4 on 2022-09-23 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0065_rename_senderid_message_received_message_sender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='received',
            new_name='receiver',
        ),
    ]
