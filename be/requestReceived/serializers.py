from rest_framework import serializers
from .models import RequestReceived

class RequestReceivedSerializers(serializers.ModelSerializer):
    class Meta:
        model = RequestReceived 
        fields = '__all__'
    def create(self, validated_data):
        return RequestReceived(**validated_data)
    
    def to_representation(self, instance):
        return super().to_representation(instance)
