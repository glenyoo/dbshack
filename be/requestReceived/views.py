# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RequestReceived
from .serializers import RequestReceivedSerializers

class RequestReceivedRequest(APIView):

    def get(self, request, format=None):
        accounts = RequestReceived.objects.all()
        return Response(accounts)
