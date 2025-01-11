from django.db import models
from django.utils.timezone import now
from companyAccount.models import CompanyAccount

# OutstandingRequest model
class OutstandingRequest(models.Model):
    REQUEST_TYPES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    ]
    requestor = models.ForeignKey(CompanyAccount, on_delete=models.CASCADE, related_name='requests_made')
    company = models.ForeignKey(CompanyAccount, on_delete=models.CASCADE, related_name='requests_received')
    carbonUnitPrice = models.FloatField(default=0)
    carbonQuantity = models.FloatField(default=0)
    requestReason = models.TextField()
    requestStatus = models.CharField(max_length=50, default='Pending Approval')
    requestType = models.CharField(max_length=4, choices=REQUEST_TYPES)
    createdDatetime = models.DateTimeField(default=now)
    updatedDatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.requestor} -> {self.target_company} ({self.request_type})"