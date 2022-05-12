from django.contrib import admin
from IraqiStore.models import News, LOV, Account, Contact, Inventory, Order, OrderItem, Product, Quote, QutoeItem


# Register your models here.
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Contact)
admin.site.register(Account)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Quote)
admin.site.register(QutoeItem)
admin.site.register(LOV)
admin.site.register(News)
