from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='map'),
    path('api/shops/', views.shops_geojson, name='shops-api'),
    path('api/nearby/', views.nearby_shops, name='nearby-api'),
]