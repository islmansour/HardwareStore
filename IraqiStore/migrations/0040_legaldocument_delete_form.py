# Generated by Django 4.0.4 on 2022-06-12 11:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0039_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactId', models.IntegerField(blank=True, null=True)),
                ('accountId', models.IntegerField(blank=True, null=True)),
                ('documentName', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Form',
        ),
    ]
