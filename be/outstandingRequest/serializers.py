from rest_framework import serializers
from .models import CompanyAccount, OutstandingRequest, RequestReceived

class OutstandingRequestSerializers(serializers.Serializer):
    class Meta:
        model = OutstandingRequest 
        fields = ['*']
