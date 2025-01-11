
from django.urls import path
from .views import ListOutstandingRequest
urlpatterns = [
    path('', ListOutstandingRequest.as_view(), name='home'),
]
