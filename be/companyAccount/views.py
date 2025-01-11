from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import CompanyAccount
from .serializers import CompanyAccountSerializers
import django.utils.timezone

class ListCompanyAccounts(APIView):

    def get(self, request, format=None):
        accounts = CompanyAccount.objects.all()
        serializer = CompanyAccountSerializers(accounts, many=True)
        return Response(serializer.data)

    def getbalancedetails(self, request, format=None):
        # retrieve companyName, carbonBalance and cashBalance from CompanyAccount
        accounts = CompanyAccount.objects.values('companyName', 'carbonBalance', 'cashBalance').all()
        return Response(accounts)
    
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