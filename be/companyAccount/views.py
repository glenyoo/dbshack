from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import CompanyAccount
from .serializers import CompanyAccountSerializers

class ListCompanyAccounts(APIView):
    def get(self, request, format=None):
        accounts = CompanyAccount.objects.all()
        serializer = CompanyAccountSerializers(accounts)
        return Response(serializer.data)
    # def post(self, request, format=None):
    #     instance = CompanyAccountSerializers(data=request.data)
    #     if instance.is_valid():
    #         instance.save()
    #         return Response('worked')
        
    #     return Response('done')
