from django.urls import path
from . import views

urlpatterns = [
    path('lov', views.get_lovs),
    path('product_list', views.get_products),
    path('inventory_list', views.get_inventory),
    path('contact_list', views.get_contacts),
    path('account_list', views.get_accounts),
    path('quote_list', views.get_quotes),
    path('quote_list_by_account/<str:accountId>', views.get_quotes_by_account),
    path('quote_list_by_contact/<contactId>', views.get_quotes_by_contact),
    path('quote_item_list', views.get_quote_item),
    path('quote_item_list_by_quote/<quoteId>', views.get_quote_item_by_quote),
    path('order_list', views.get_orders),
    path('order_list_by_account/<str:accountId>', views.get_orders_by_account),
    path('order_list_by_contact/<contactId>', views.get_orders_by_contact),
    path('order_item_list/<orderId>', views.get_order_item_by_order),
    path('get_single_inventory/<str:pk>', views.get_single_inventory),
    path('get_user/<str:pk>', views.get_user_by_uid),
    path('news_list', views.get_news),
    path('delivery_list', views.get_deliverys),
    path('delivery_list_by_account', views.get_deliverys_by_account),
    path('delivery_list_by_contact', views.get_deliverys_by_contact),
    path('single_product/<str:pk>', views.get_single_product),
    path('single_inventory/<str:pk>', views.get_single_inventory),
    path('single_contact/<str:pk>', views.get_single_contact),
    path('single_account/<str:pk>', views.get_single_account),
    path('single_quote/<str:pk>', views.get_single_quote),
    path('single_order/<str:pk>', views.get_single_order),
    path('single_news/<str:pk>', views.get_single_news),
    path('single_delivery/<str:pk>', views.get_deliverys),
    path('upsert_product/<str:pk>', views.upsert_product),
    path('upsert_inventory/<str:pk>', views.upsert_inventory),
    path('upsert_contact/<str:pk>', views.upsert_contact),
    path('upsert_account/<str:pk>', views.upsert_account),
    path('upsert_quote/<str:pk>', views.upsert_quote),
    path('upsert_quote_item/<str:pk>', views.upsert_quote_item),
    path('upsert_order/<str:pk>', views.upsert_order),
    path('upsert_order_item/<str:pk>', views.upsert_order_item),
    path('upsert_news/<str:pk>', views.upsert_news),
    path('upsert_delivery/<str:pk>', views.upsert_delivery),
    path('delete_order_item/<str:pk>', views.delete_order_item),
    path('delete_quote_item/<str:pk>', views.delete_quote_item),
    path('get_account_contacts/<str:pk>', views.get_account_contacts)


]
