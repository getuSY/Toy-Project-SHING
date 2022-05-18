from django.db import models

# Create your models here.
class Station(models.Model):
    line = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    code = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
    # scaffold = models.BooleanField()
    # wheelchair = models.BooleanField()
    # lactation = models.BooleanField()
    # slope_wheel = models.BooleanField()
    # slope_bicycle = models.BooleanField()
