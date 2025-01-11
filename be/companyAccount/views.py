from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import CompanyAccount
from .serializers import CompanyAccountSerializers
from rest_framework.permissions import IsAuthenticated
from user.models import CustomUser

class ListCompanyAccounts(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        print(request.user.username)
        company_id = CustomUser.objects.get(username=request.user.username).company_id
        accounts = CompanyAccount.objects.get(id=company_id)
        serializer = CompanyAccountSerializers(accounts)
        return Response(serializer.data)
    # def post(self, request, format=None):
    #     instance = CompanyAccountSerializers(data=request.data)
    #     if instance.is_valid():
    #         instance.save()
    #         return Response('worked')
        
    #     return Response('done')

    def getbalancedetails(self, request, format=None):
        # retrieve companyName, carbonBalance and cashBalance from CompanyAccount
        accounts = CompanyAccount.objects().values('companyName', 'carbonBalance', 'cashBalance')
        return Response(accounts)
    
    def post(self, request, format=None):
        serializer = CompanyAccountSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, format=None):
        serializer = CompanyAccountSerializers(data=request.data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, format=None):
        serializer = CompanyAccountSerializers(data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)