from django.urls import path
from . import views

urlpatterns = [
    path('product_list', views.get_data),
    path('inventory_list', views.get_inventory),
    path('contact_list', views.get_contacts),
    path('account_list', views.get_accounts),
    path('quote_list', views.get_quote),
    path('quote_item_list', views.get_quote_item),
    path('order_list', views.get_order),
    path('order_item_liat', views.get_order_item),


]
