# Generated by Django 4.0.4 on 2022-07-29 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0054_news_img_news_productid_alter_order_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='img',
            new_name='url',
        ),
        migrations.AlterField(
            model_name='news',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
