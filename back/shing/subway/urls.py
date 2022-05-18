from django.urls import path
from . import views

app_name = 'subway'
urlpatterns = [
    path('create/transferstation/', views.read_transfer_station)
]
