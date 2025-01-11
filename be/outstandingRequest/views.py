from rest_framework.views import APIView
from rest_framework.response import Response
from .models import OutstandingRequest
from .models import CompanyAccount
from .serializers import OutstandingRequestSerializers

class ListOutstandingRequest(APIView):

    
    def getall(self, request, format=None):
        accounts = OutstandingRequest.objects().all()
        return Response(accounts)
    
    def get(self, request, format=None):
        companyId = request.query_params.get('companyId')
        if companyId is not None:
            accounts = OutstandingRequest.objects().filter(companyId=companyId).all()
            # check for param type and filter data type
            return Response(accounts)
        return Response("Please provide companyId")

        # accounts = OutstandingRequest.objects().values('companyId', 'createdDatetime', 'carbonUnitPrice', 'carbonQuantity', 'requestStatus', 'requestType')
        # return Response(accounts)
    
    def post(self, request, format=None):
        # debug: date time format
        serializer = OutstandingRequestSerializers(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, format=None):
        serializer = OutstandingRequestSerializers(request.data)
        # check if the company id exists
        # companyId
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=201)
    
    def delete(self, request, format=None):
        outstandingRequestId = request.query_params.get('id')
        serializer = OutstandingRequestSerializers(data=request.data)

        if outstandingRequestId is not None:
            request = OutstandingRequest.objects().filter(outstandingRequestId=outstandingRequestId).delete()
            return Response(request, status=201)
        return Response(serializer.errors, status=400)
    
