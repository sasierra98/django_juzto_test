import datetime

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from product.serializers import ProductSerializer


class ProductAPIView(APIView):
    serializer_class = ProductSerializer

    def get(self, request, format=None):
        product = Product.objects.all().order_by('id')
        serializer = self.serializer_class(product, many=True)
        return Response(serializer.data)

    def post(self, request):
        body = request.data

        serializer = self.serializer_class(data=body)
        if serializer.is_valid():
            serializer.save()
            return Response('Created', status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class DetailProductAPIView(APIView):
    serializer_class = ProductSerializer

    def get(self, request, pk, format=None):
        product = Product.objects.filter(pk=pk).first()
        serializer = self.serializer_class(product)
        return Response(serializer.data)

    def put(self, request, pk):
        body = request.data

        product = Product.objects.filter(pk=pk).first()

        if product:
            serializer = self.serializer_class(product, data=body)
            if serializer.is_valid():
                serializer.save()
                return Response('Updated', status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors)
        else:
            return Response('Not found', status=status.HTTP_200_OK)

    def delete(self, request, pk):
        product = Product.objects.filter(pk=pk).first()
        if product:
            product.delete()
            return Response('Deleted', status=status.HTTP_204_NO_CONTENT)
        else:
            return Response('Not found', status=status.HTTP_200_OK)
