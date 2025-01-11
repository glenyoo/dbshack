from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CompanyAccount, OutstandingRequest, RequestReceived
from .serializers import OutstandingRequestSerializers

class ListOutstandingRequest(APIView):

    def get(self, request, format=None):
        accounts = OutstandingRequest.objects.all()
        return Response(accounts)
