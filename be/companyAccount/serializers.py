from rest_framework import serializers
from .models import CompanyAccount, OutstandingRequest, RequestReceived

class CompanyAccountSerializers(serializers.Serializer):
    class Meta:
        model = CompanyAccount 
        fields = ['*']
