from import_export import resources
from FoodsApi import models

class japanese_food_standard_ingredients_listResource(resources.ModelResource):
    class Meta:
        model = models.japanese_food_standard_ingredients_list
        import_id_fields = ['INDEX_NUM']

class five_nutrientsResource(resources.ModelResource):
    class Meta:
        model = models.five_nutrients
        import_id_fields = ['food_id']

class foodResource(resources.ModelResource):
    class Meta:
        model = models.food
        import_id_fields = ['food_id']
