from django.db import models

# Create your models here.
class Station(models.Model):
    line = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    code = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
    # lactation = models.BooleanField()
    # slope_bicycle = models.BooleanField()
    # scaffold = models.BooleanField()
    # wheelchair = models.BooleanField()
    # slope_wheel = models.BooleanField()
    

    def __str__(self):
        return self.name


class TransferStation(models.Model):
    id = models.IntegerField(primary_key=True)
    line = models.IntegerField()
    name = models.CharField(max_length=10)
    transfer_line = models.CharField(max_length=10)
    transfer_distance = models.IntegerField()
    transfer_time = models.CharField(max_length=10)

    def __str__(self):
        return self.transfer_line + self.name
        

class WheelchairSlope(models.Model):
    line = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    total = models.IntegerField()


class WheelchairSlopeLocation(models.Model):
    slope_station = models.ForeignKey(WheelchairSlope, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
