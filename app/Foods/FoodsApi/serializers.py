from FoodsApi import models
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

class foodSerializer(serializers.ModelSerializer):
    """
    食材テーブルシリアライザ
    """
    class Meta:
        model = models.food
        fields = ['food_id'
                , 'food_name_1'
                , 'food_status']

class fiveNutrientsSerializer(serializers.ModelSerializer):
    """
    五大栄養素テーブルシリアライザ
    """
    class Meta:
        model = models.five_nutrients
        fields = ['food_group'
                ,'energy_kcal'
                ,'energy_kj'
                ,'protain'
                ,'fat'
                ,'carbohydrates'
                ,'mineral_Na'
                ,'mineral_Ka'
                ,'mineral_Ca'
                ,'mineral_P'
                ,'mineral_Fe'
                ,'vitamin_A'
                ,'vitamin_B1'
                ,'vitamin_B2'
                ,'vitamin_Niacin'
                ,'vitamin_C'
                ,'NaCl_EQ'
                ,'fibtg'
                ,'cholesterol']

class detailNutrientsSerializer(WritableNestedModelSerializer):
    """
    日本食品標準成分表2015年版（七訂）テーブルシリアライザ
    """
    class Meta:
        model = models.japanese_food_standard_ingredients_list
        fields = ['FOOD_GROUP'
                    ,'REFUSE'
                    ,'ENERC_KCAL'
                    ,'ENERC'
                    ,'WATER'
                    ,'PROTAIN'
                    ,'PROTCAA'
                    ,'FAT'
                    ,'FATNLEA'
                    ,'FASAT'
                    ,'FAMS'
                    ,'FAPU'
                    ,'CHOLE'
                    ,'CARBOHYDRATES'
                    ,'CHOAVLM'
                    ,'FIBSOL'
                    ,'FIBINS'
                    ,'FIBTG'
                    ,'ASH'
                    ,'NA'
                    ,'K'
                    ,'CA'
                    ,'MG'
                    ,'P'
                    ,'FE'
                    ,'ZN'
                    ,'CU'
                    ,'MN'
                    ,'ID'
                    ,'SE'
                    ,'CR'
                    ,'MO'
                    ,'RETOL'
                    ,'CARTA'
                    ,'CARTB'
                    ,'CRYPXB'
                    ,'CARTBEQ'
                    ,'VITA_RAE'
                    ,'VITD'
                    ,'TOCPHA'
                    ,'TOCPHB'
                    ,'TOCPHG'
                    ,'TOCPHD'
                    ,'VITK'
                    ,'THIAHCL'
                    ,'RIBF'
                    ,'NIA'
                    ,'VITB6A'
                    ,'VITB12'
                    ,'FOL'
                    ,'PANTAC'
                    ,'BIOT'
                    ,'VITC'
                    ,'NACL_EQ'
                    ,'ALC'
                    ,'NITRA'
                    ,'THEBRN'
                    ,'CAFFN'
                    ,'TAN'
                    ,'POLYPHENT'
                    ,'ACEAC'
                    ,'COOKING_OIL'
                    ,'OA'
                    ,'RATE_OF_CHANGE_IN_WEIGHT']

class foodsFiveSerializer(WritableNestedModelSerializer):
    """
    五大栄養素と食品名の対応付けシリアライザ
    """
    nutrients_five = fiveNutrientsSerializer()
    class Meta:
        model = models.food
        fields = ['food_id', 'food_name_1', 'nutrients_five']

class foodsDetailSerializer(WritableNestedModelSerializer):
    """
    詳細栄養素と食品名の紐づけシリアライザ
    """
    nutrients_detail = detailNutrientsSerializer()
    class Meta:
        model = models.food
        fields = ['food_id', 'food_name_1', 'nutrients_detail']

