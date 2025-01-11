from rest_framework import serializers
from .models import RequestReceived

class RequestReceivedSerializers(serializers.Serializer):
    class Meta:
        model = RequestReceived 
        fields = ['*']
