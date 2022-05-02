from rest_framework import serializers
from IraqiStore.models import Account, Contact, Product, Inventory


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
