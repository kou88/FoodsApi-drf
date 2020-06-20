from FoodsApi import models
from rest_framework import serializers

class foodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.food
        fields = ['food_id', 'food_name_hiragana']

class fiveNutrientsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.five_nutrients
        fields = ['pk', 'food_name']    

class detailNutrientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.japanese_food_standard_ingredients_list
        fields = '__all__'

    
