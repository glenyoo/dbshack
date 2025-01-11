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
        pass
        # companyId needed from params
        # companyId = request.query_params.get('companyId')
        # if companyId is not None:
        #     accounts = RequestReceived.objects.filter(companyId=companyId).all()
        #     return Response(accounts)
        # return Response("Please provide companyId")
    
        # accounts = RequestReceived.objects.values('companyName', 'carbonBalance', 'cashBalance').all()
        # return Response(accounts)
    
    def post(self, request, format=None):
        createdDatetime = django.utils.timezone.now()
        updatedDatetime = createdDatetime
        request.data['createdDatetime'] = createdDatetime
        request.data['updatedDatetime'] = updatedDatetime
        serializer = CompanyAccountSerializers(request.data)
        # serializer = CompanyAccountSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, format=None):
        request.data['updatedDatetime'] = timezone.now()
        serializer = CompanyAccountSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, format=None):
        # not tested
        serializer = CompanyAccountSerializers(data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    # def getall(self, request, format=None):
    #     accounts = RequestReceived.objects().all()
    #     return Response(accounts)
    
    # def get(self, request, format=None):
    #     companyId = request.query_params.get('companyId')
    #     if companyId is not None:
    #         accounts = OutstandingRequest.objects().filter(companyId=companyId).all()
    #         # check for param type and filter data type
    #         return Response(accounts)
    #     return Response("Please provide companyId")

    #     # accounts = OutstandingRequest.objects().values('companyId', 'createdDatetime', 'carbonUnitPrice', 'carbonQuantity', 'requestStatus', 'requestType')
    #     # return Response(accounts)
    
    # def post(self, request, format=None):
    #     # debug: date time format
    #     createdDatetime = django.utils.timezone.now()
    #     updatedDatetime = createdDatetime
    #     request.data['createdDatetime'] = createdDatetime
    #     request.data['updatedDatetime'] = updatedDatetime
    #     serializer = OutstandingRequestSerializers(request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)
    
    # def put(self, request, format=None):
    #     serializer = OutstandingRequestSerializers(data=request.data)
    #     updateDatetime = django.utils.timezone.now()
    #     request.data['updatedDatetime'] = updateDatetime
    #     # check if the company id exists
    #     # companyId
    #     if serializer.is_valid():
    #         serializer.update()
    #         return Response(serializer.data, status=201)
    
    # def delete(self, request, format=None):
    #     outstandingRequestId = request.query_params.get('id')
    #     serializer = OutstandingRequestSerializers(data=request.data)

    #     if outstandingRequestId is not None:
    #         request = OutstandingRequest.objects().filter(outstandingRequestId=outstandingRequestId).delete()
    #         return Response(request, status=201)
    #     return Response(serializer.errors, status=400)
   