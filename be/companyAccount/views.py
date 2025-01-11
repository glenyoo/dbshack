from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CompanyAccount
from .serializers import CompanyAccountSerializers

class ListCompanyAccounts(APIView):

    def get(self, request, format=None):
        accounts = CompanyAccount.objects.all()
        return Response(accounts)
