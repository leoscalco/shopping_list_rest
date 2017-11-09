from .models import ItemInList, Item, ShoppingList
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'name')

class ItemInListSerializer(serializers.ModelSerializer):
    # shopping_list = ShoppingListSerializer()
    # item = ItemSerializer()
    shopping_list = serializers.IntegerField(source='shopping_list.id')
    # shopping_list_date = serializers.ReadOnlyField(source='shopping_list.date')
    # shopping_list = serializers.IntegerField(source='item.id')
    item_name = serializers.CharField(source='item.name')

    class Meta:
        model = ItemInList
        fields = ('item_name', 'shopping_list', 'amount', 'already_bought')

    def create(self, validated_data):
        # print self.data['item_name']
        try:
            item = Item.objects.get(name=self.data['item_name'])
        except Item.DoesNotExist:
            item = Item.objects.create(name=self.data['item_name'])

        shopping_list = ShoppingList.objects.get(id=self.data['shopping_list'])

        iteminlist = ItemInList.objects.create(item=item,
            amount=self.data['amount'], shopping_list=shopping_list)

        return iteminlist

class ShoppingListSerializer(serializers.ModelSerializer):
    itens = ItemInListSerializer(source="iteminlist_set", many=True)

    class Meta:
        model = ShoppingList
        fields = ('id', 'date', 'itens')

    def create(self, validated_data):
        arr_itens = []
        arr = self.data['itens']

        for a in arr:
            try:
                item = Item.objects.get(name=a['item_name'])
            except:
                item = Item.objects.create(name=a['item_name'])

            arr_itens.append(item)

        shopping_list = ShoppingList.objects.create()

        counter = 0
        for i in arr_itens:
            iteminlist = ItemInList.objects.create(item=i,
                amount=arr[counter]['amount'],
             shopping_list=shopping_list)
            counter+=1

        return shopping_list