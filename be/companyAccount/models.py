from django.db import models
from django.utils.timezone import now

# CompanyAccount model
class CompanyAccount(models.Model):
    companyName = models.CharField(max_length=256)
    carbonBalance = models.IntegerField(default=0)
    cashBalance = models.FloatField(default=0.00)
    activeAccount = models.BooleanField(default=True)
    createdDatetime = models.DateTimeField(default=now)
    updatedDatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.companyName