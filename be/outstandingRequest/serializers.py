from rest_framework import serializers
from .models import OutstandingRequest

class OutstandingRequestSerializers(serializers.Serializer):
    class Meta:
        model = OutstandingRequest 
        fields = ['*']
