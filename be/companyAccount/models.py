from django.db import models
from django.utils.timezone import now

# CompanyAccount model
class CompanyAccount(models.Model):
    company_name = models.CharField(max_length=256)
    carbon_balance = models.IntegerField(default=0)
    cash_balance = models.FloatField(default=0.00)
    active_account = models.BooleanField(default=True)
    created_datetime = models.DateTimeField(default=now)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name