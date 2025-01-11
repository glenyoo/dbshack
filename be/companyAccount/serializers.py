from rest_framework import serializers
from .models import CompanyAccount

class CompanyAccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyAccount 
        fields = '__all__'
    def create(self, validated_data):
        return CompanyAccount(**validated_data)
    
    def to_representation(self, instance):
        return super().to_representation(instance)
