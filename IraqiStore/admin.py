from django.contrib import admin
from IraqiStore.models import AccountContacts, Message, CronTest, Delivery, LegalDocument, News, LOV, Account, Contact, Inventory, Notification, NotificationRecipient, Order, OrderItem, Product, Quote, QutoeItem, User


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
admin.site.register(Delivery)
admin.site.register(User)
admin.site.register(LegalDocument)
admin.site.register(AccountContacts)
admin.site.register(CronTest)
admin.site.register(Notification)
admin.site.register(NotificationRecipient)
admin.site.register(Message)
