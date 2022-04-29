from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from IraqiStore.models import Product
from .serializers import productSerializer


def iraqi_view(request):
    return HttpResponse('hello')

# Create your views here.


@api_view(['GET'])
def get_data(request):
    products = Product.objects.all()
    serializer = productSerializer(products, many=True)
    return Response(serializer.data)
