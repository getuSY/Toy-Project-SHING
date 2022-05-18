from django.http import HttpResponse
from django.shortcuts import render
import csv
from .models import Station, TransferStation

# Create your views here.
def read_transfer_station(request):
    path = 'csv\서울교통공사_환승역거리소요시간정보_20210701.csv'
    file = open(path, 'r')
    reader = csv.reader(file)
    lst = list()
    for row in reader:
        lst.append(TransferStation(line=row[1], name=row[2], transfer_line=row[3], transfer_distance=row[4], transfer_time=row[5]))
    TransferStation.objects.bulk_create(lst)
    return HttpResponse('Transfer Station DB created')
