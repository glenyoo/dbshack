
from django.urls import path
from .views import RequestReceivedRequest
urlpatterns = [
    path('', RequestReceivedRequest.as_view(), name='home'),
]
