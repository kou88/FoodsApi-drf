from django.contrib import admin
from FoodsApi import models
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from . import resources

@admin.register(models.food)
class foodAdmin(ImportExportModelAdmin):
    """ 食材テーブル """
    resource_class = resources.foodResource
    list_display = ['food_id','food_name_1']
    list_display_links = ['food_id']

@admin.register(models.japanese_food_standard_ingredients_list)
class japanese_food_standard_ingredients_listAdmin(ImportExportModelAdmin):
    """ 日本食品標準成分表2015年版（七訂）テーブル """
    resource_class = resources.japanese_food_standard_ingredients_listResource
    list_display = ['FOOD_GROUP','FOOD_NUM','Tagnames']
    list_display_links = ['FOOD_NUM']

admin.site.register(models.food_jfsil_relations)
admin.site.register(models.five_nutrients)
admin.site.register(models.nutrients_list)