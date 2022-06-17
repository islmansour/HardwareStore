from rest_framework import serializers
from IraqiStore.models import AccountContacts, File, LOV, Account, Contact, Delivery, LegalDocument, News, Order, OrderItem, Product, Inventory, Quote, QutoeItem, User


# Serializers define the API representation.


class FileSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False)


class lovSerializer(serializers.ModelSerializer):
    class Meta:
        model = LOV
        fields = '__all__'


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class inventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class legalDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalDocument
        fields = '__all__'


class accountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class orderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class orderSerializer(serializers.ModelSerializer):
    orderItems = orderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'orderDate', 'accountId', 'contactId', 'status', 'order_number', 'street',
                  'street2', 'town', 'wazeLink', 'notes', 'quoteId', 'deliveryId', 'created', 'created_by', 'orderItems']


class quoteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = QutoeItem
        fields = '__all__'


class quoteSerializer(serializers.ModelSerializer):
    quoteItems = quoteItemSerializer(many=True, read_only=True)

    class Meta:
        model = Quote
        fields = ['id', 'quoteDate', 'accountId', 'contactId', 'status',
                  'quote_number', 'delivery', 'notes', 'created', 'created_by', 'quoteItems']


class newsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class deliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'


class AccountContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountContacts
        fields = '__all__'
