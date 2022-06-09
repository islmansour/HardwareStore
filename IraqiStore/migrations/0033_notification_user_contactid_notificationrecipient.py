# Generated by Django 4.0.4 on 2022-06-08 13:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0032_orderitem_discount_qutoeitem_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=256, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('sent', models.BooleanField(default=True)),
                ('target', models.IntegerField(blank=True, null=True)),
                ('action', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='contactId',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='NotificationRecipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seen', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('messageId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificationRecipients', to='IraqiStore.notification')),
                ('recipientId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificationRecipients', to='IraqiStore.user')),
            ],
        ),
    ]