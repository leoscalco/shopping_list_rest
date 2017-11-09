# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Item, ShoppingList, ItemInList
from .serializers import ItemSerializer, ShoppingListSerializer, ItemInListSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

# Create your views here.

class ItemList(APIView):
    """
    List all itens, or create a new item
    """
    def get(self, request, format=None):
        itens = Item.objects.all()
        serializer = ItemSerializer(itens, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemDetail(APIView):
    """
    Detail, update or delete an item
    """

    def get_object(self, pk):
        try:
            return Item.objects.get(id=pk)
        except Item.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        Item.delete(item)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ShoppingListList(APIView):
    """
    List all shopping lists, or create a new one
    """
    def get(self, request, format=None):
        shopping_lists = ShoppingList.objects.all()
        serializer = ShoppingListSerializer(shopping_lists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShoppingListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ItemInListList(APIView):
    """
    List all itens in shopping list, or create a new one
    """
    def get(self, request, format=None):
        itens = ItemInList.objects.all()
        serializer = ItemInListSerializer(itens, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ItemInListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemInListDetail(APIView):
    """
    Detail, update or delete an item in list
    """

    def get_object(self, pk):
        try:
            return ItemInList.objects.get(id=pk)
        except ItemInList.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        iteminlist = self.get_object(pk)
        serializer = ItemInListSerializer(iteminlist)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        iteminlist = self.get_object(pk)
        serializer = ItemInListSerializer(iteminlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        iteminlist = self.get_object(pk)
        ItemInList.delete(iteminlist)
        return Response(status=status.HTTP_204_NO_CONTENT)