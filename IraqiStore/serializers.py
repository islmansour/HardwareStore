from rest_framework import serializers
from IraqiStore.models import LOV, Account, Contact, Delivery, News, Order, OrderItem, Product, Inventory, Quote, QutoeItem, User


class lovSerializer(serializers.ModelSerializer):
    class Meta:
        model = LOV
        fields = ('type', 'name', 'value')


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


class newsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class deliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'
