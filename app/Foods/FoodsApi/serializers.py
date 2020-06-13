from FoodsApi import models
from rest_framework import serializers

class foodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.food
        fields = ['food_id', 'food_name_hiragana']

class fiveNfutrientsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.five_nutrients
        fields = '__all__'    

class japanese_food_standard_ingredients_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.japanese_food_standard_ingredients_list
        fields = '__all__'

class items(serializers.ModelSerializer):
    class Meta:
        model = models.japanese_food_standard_ingredients_list
        fiels = ['FOOD_GROUP', 'Tagnames', 'VITAMINA']
    
