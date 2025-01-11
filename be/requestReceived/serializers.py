from rest_framework import serializers
from .models import CompanyAccount, OutstandingRequest, RequestReceived

class RequestReceivedSerializers(serializers.Serializer):
    class Meta:
        model = RequestReceived 
        fields = ['*']
