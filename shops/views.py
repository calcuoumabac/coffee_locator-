from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from .models import CoffeeShop

# Renders the map page
def map_view(request):
    return render(request, 'map.html')

# Returns all shops as GeoJSON
def shops_geojson(request):
    shops = CoffeeShop.objects.all()
    return JsonResponse(
        serialize('geojson', shops, geometry_field='location', fields=('name', 'address')),
        safe=False
    )

# Returns nearby shops based on user location
def nearby_shops(request):
    lat = float(request.GET.get('lat', 40.7128))
    lng = float(request.GET.get('lng', -74.0060))
    
    user_location = Point(lng, lat, srid=4326)
    
    nearby = CoffeeShop.objects.annotate(
        distance=Distance('location', user_location)
    ).filter(distance__lte=2000).order_by('distance')  # 2km radius
    
    return JsonResponse(
        serialize('geojson', nearby, geometry_field='location', fields=('name', 'address')),
        safe=False
    )