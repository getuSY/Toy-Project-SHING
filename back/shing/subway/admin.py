from django.contrib import admin
from .models import Station, TransferStation

# Register your models here.
admin.site.register(Station)
admin.site.register(TransferStation)