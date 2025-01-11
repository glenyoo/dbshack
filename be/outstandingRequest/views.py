from rest_framework.views import APIView
from rest_framework.response import Response
from .models import OutstandingRequest
from .models import CompanyAccount
from .serializers import OutstandingRequestSerializers

class ListOutstandingRequest(APIView):

    def get(self, request, format=None):
        accounts = OutstandingRequest.objects.all()
        serializer = OutstandingRequestSerializers(accounts, many=True)
        return Response(serializer.data)
    
    def getRequestReceived(self, request, format=None):
        accounts = OutstandingRequest.objects.all()
        return Response(accounts)
    
    def post(self, request, format=None):
        serializer = OutstandingRequestSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, format=None):
        serializer = OutstandingRequestSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, format=None):
        # not tested
        serializer = OutstandingRequestSerializers(data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
