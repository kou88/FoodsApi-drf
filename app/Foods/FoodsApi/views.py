from FoodsApi import models
from FoodsApi import serializers
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

class foodViewSet(viewsets.ReadOnlyModelViewSet):
    """
    food api
    """
    def list(self, request):
        queryset = models.food.objects.all()
        serializer_class = serializers.foodSerializer
        return Response(serializer.data)

class fiveNutrientsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    five nutrients api
    """
    queryset = models.five_nutrients.objects.all()
    serializer_class = serializers.fiveNfutrientsSerializer

class allNutrientsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    japanese_food_standard_ingredients_list api
    """
    queryset = models.japanese_food_standard_ingredients_list.objects.all()
    serializer_class = serializers.japanese_food_standard_ingredients_listSerializer

# class searchFiveNutrientsViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     search five nutrients api
#     """
#     queryset = models.five_nutrients.objects.all()
#     serializer_class = serializers.fiveNfutrientsSerializer
#     lookup_field = ('food_name')

#     def get_queryset(self):
#         queryset = models.five_nutrients.objects.all()
#         food_name = self.request.query_params.get('food_name', None)
#         if food_name is not None:
#             queryset = queryset.filter(food_name__icontains=food_name)
#         return queryset

class HowToTest():
    def returnTrue():
        return True
