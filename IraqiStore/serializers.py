from rest_framework import serializers
from IraqiStore.models import Account, Contact, Order, OrderItem, Product, Inventory, Quote, QutoeItem


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class inventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class accountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class orderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class quoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


class quoteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = QutoeItem
        fields = '__all__'
