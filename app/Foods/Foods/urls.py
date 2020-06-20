"""Foods URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from FoodsApi import views

router = routers.DefaultRouter()
# router.register(r'', views.foodViewSet)
# router.register(r'nutrients', views.)
router.register(r'nutrients/all', views.allNutrientsViewSet)
router.register(r'nutrients/five', views.fiveNutrientsViewSet)
# router.register(r'foods', views.foodViewSet)
# router.register(r'foods/search?q=', views.foodViewSet)
# router.register(r'foods/{food_id}', views)
# router.register(r'foods/{food_id}/description', views)
# router.register(r'foods/{food_id}/status', views)
# router.register(r'foods/{food_id}/nutrients/five', views)
# router.register(r'foods/{food_id}/nutrients/detail', views)

urlpatterns = [
    path('foods-api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]
