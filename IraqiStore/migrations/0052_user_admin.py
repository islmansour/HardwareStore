# Generated by Django 4.0.4 on 2022-07-07 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0051_user_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]