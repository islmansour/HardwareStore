from django.contrib import admin
from IraqiStore.models import Account, Contact, Inventory, Order, OrderItem, Product, Quote, QutoeItem


# Register your models here.
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Contact)
admin.site.register(Account)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Quote)
admin.site.register(QutoeItem)
