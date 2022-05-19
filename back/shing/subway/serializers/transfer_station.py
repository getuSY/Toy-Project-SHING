from rest_framework import serializers
from ..models import TransferStation

class TransferStationSerializer(serializers.ModelSerializer):

    model = TransferStation
    fields = '__all__'