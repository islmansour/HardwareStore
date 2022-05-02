from django.urls import path
from . import views

urlpatterns = [
    path('product_list', views.get_data),
    path('inventory_list', views.get_inventory),
    path('contact_list', views.get_contacts),
    path('account_list', views.get_accounts)


]
