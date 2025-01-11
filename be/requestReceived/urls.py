
from django.urls import path
from .views import ListRequestReceived
urlpatterns = [
    path('', ListRequestReceived.as_view(), name='home'),
]
