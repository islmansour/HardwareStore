# Generated by Django 4.0.4 on 2022-05-02 21:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('IraqiStore', '0005_alter_account_ceeated_by_alter_account_contact_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderDate', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[(1, 'חדשה'), (2, 'מאושרת'), (3, 'ממתינה לאישור'), (4, 'בדרך ללקוח'), (5, 'נמסר'), (6, 'מבוטלת')], default='1', max_length=32)),
                ('street', models.CharField(blank=True, max_length=255, null=True)),
                ('street2', models.CharField(blank=True, max_length=255, null=True)),
                ('town', models.CharField(blank=True, max_length=50, null=True)),
                ('wazeLink', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('ceeated_by', models.IntegerField(blank=True, null=True)),
                ('accountId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='IraqiStore.account')),
                ('contactId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='IraqiStore.contact')),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quoteDate', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[(1, 'חדשה'), (2, 'מאושרת'), (3, 'ממתינה לאישור'), (4, 'מבוטלת')], default='1', max_length=32)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('ceeated_by', models.IntegerField(blank=True, null=True)),
                ('accountId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='IraqiStore.account')),
                ('contactId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='IraqiStore.contact')),
            ],
        ),
        migrations.CreateModel(
            name='QutoeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('ceeated_by', models.IntegerField(blank=True, null=True)),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='IraqiStore.product')),
                ('quoteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IraqiStore.quote')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('ceeated_by', models.IntegerField(blank=True, null=True)),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IraqiStore.order')),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='IraqiStore.product')),
                ('quoteItemId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='IraqiStore.qutoeitem')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='quoteId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='IraqiStore.quote'),
        ),
    ]
