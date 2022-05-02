from django.contrib import admin
from IraqiStore.models import Account, Contact, Inventory, Product


# Register your models here.
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Contact)
admin.site.register(Account)
