
from django.urls import path
from .views import ListCompanyAccounts
urlpatterns = [
    path('', ListCompanyAccounts.as_view(), name='home'),
]
