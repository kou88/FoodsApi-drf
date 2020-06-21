from FoodsApi import models
from FoodsApi import serializers
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView

class FoodViewSet(viewsets.ReadOnlyModelViewSet):
    """
    food api
    """
    def list(self, request):
        queryset = models.food.objects.all()
        serializer_class = serializers.foodSerializer
        return Response(serializer.data)

class FoodsFiveViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.food.objects.all()
    serializer_class = serializers.foodsFiveSerializer

class FoodsDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.food.objects.all()
    serializer_class = serializers.foodsDetailSerializer

class SearchFoodsFiveViewSet(viewsets.ReadOnlyModelViewSet):
    """
    search five nutrients api
    """
    queryset = models.food.objects.all()
    serializer_class = serializers.foodSerializer

    def get_queryset(self):
        queryset = models.food.objects.all()
        food_name_1 = self.request.query_params.get('q', None)
        if food_name_1 is not None:
            queryset = queryset.filter(food_name_1__icontains=food_name_1)
        return queryset

class HowToTest():
    def returnTrue():
        return True
