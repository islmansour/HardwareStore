from django.urls import path
from . import views

urlpatterns = [
    path('lov', views.get_lovs),
    path('product_list', views.get_products),
    path('inventory_list', views.get_inventory),
    path('contact_list', views.get_contacts),
    path('account_list', views.get_accounts),
    path('quote_list', views.get_quotes),
    path('quote_item_list', views.get_quote_item),
    path('order_list', views.get_orders),
    path('order_item_liat', views.get_order_item),
    path('single_product/<str:pk>', views.get_single_product),
    path('single_inventory/<str:pk>', views.get_single_inventory),
    path('single_contact/<str:pk>', views.get_single_contact),
    path('single_account/<str:pk>', views.get_single_account),
    path('single_quote/<str:pk>', views.get_single_quote),
    path('single_order/<str:pk>', views.get_single_order),
    path('upsert_product/<str:pk>', views.upsert_product),
    path('upsert_inventory/<str:pk>', views.upsert_inventory),
    path('upsert_contact/<str:pk>', views.upsert_contact),
    path('upsert_account/<str:pk>', views.upsert_account),
    path('upsert_quote/<str:pk>', views.upsert_quote),
    path('upsert_quote_item/<str:pk>', views.upsert_quote_item),
    path('upsert_order/<str:pk>', views.upsert_order),
    path('upsert_order_item/<str:pk>', views.upsert_order_item),


]
