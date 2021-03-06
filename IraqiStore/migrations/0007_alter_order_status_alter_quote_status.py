# Generated by Django 4.0.4 on 2022-05-02 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0006_order_quote_qutoeitem_orderitem_order_quoteid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('1', 'חדשה'), ('2', 'מאושרת'), ('3', 'ממתינה לאישור'), ('4', 'בדרך ללקוח'), ('5', 'נמסר'), ('6', 'מבוטלת')], default='1', max_length=32),
        ),
        migrations.AlterField(
            model_name='quote',
            name='status',
            field=models.CharField(choices=[('1', 'חדשה'), ('2', 'מאושרת'), ('3', 'ממתינה לאישור'), ('4', 'מבוטלת')], default=1, max_length=32),
        ),
    ]
