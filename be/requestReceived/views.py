# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RequestReceived
from .serializers import RequestReceivedSerializers

class ListRequestReceived(APIView):
    def get(self, request, format=None):
        accounts = RequestReceived.objects.all()
        serializer = RequestReceivedSerializers(accounts, many=True)
        return Response(serializer.data)
    
    def getRequestReceived(self, request, format=None):
        accounts = RequestReceived.objects.all()
        return Response(accounts)
    
    def post(self, request, format=None):
        serializer = RequestReceivedSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, format=None):
        serializer = RequestReceivedSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, format=None):
        # not tested
        serializer = RequestReceivedSerializers(data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
