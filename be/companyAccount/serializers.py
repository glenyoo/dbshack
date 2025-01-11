from rest_framework import serializers
from .models import CompanyAccount

class CompanyAccountSerializers(serializers.Serializer):
    class Meta:
        model = CompanyAccount 
        fields = ['*']
