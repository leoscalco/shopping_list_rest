# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class ShoppingList(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    itens = models.ManyToManyField(Item, through="ItemInList")

    def __unicode__(self):
        return "Lista de Compras - " + self.date.strftime("%d/%m/%Y %H:%M")

    def __str__(self):
        return "Lista de Compras - " + self.date.strftime("%d/%m/%Y %H:%M")

class ItemInList(models.Model):
    item = models.ForeignKey(Item)
    shopping_list = models.ForeignKey(ShoppingList)
    amount = models.IntegerField(default=1)
    already_bought = models.BooleanField(default=False)

    def __unicode__(self):
        return "Lista: " + str(self.shopping_list.id) + " - " + self.item.name

    def __str__(self):
        return "Lista: " + str(self.shopping_list.id) + " - " + self.item.name

