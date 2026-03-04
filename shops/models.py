from django.contrib.gis.db import models

class CoffeeShop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    # This is the GeoDjango magic!
    location = models.PointField()  # Stores lat/long
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Coffee Shops"