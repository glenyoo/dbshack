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
    carbon_unit_price = models.FloatField(default=0)
    carbon_quantity = models.FloatField(default=0)
    request_reason = models.TextField()
    request_status = models.CharField(max_length=50, default='Pending Approval')
    request_type = models.CharField(max_length=4, choices=REQUEST_TYPES)
    created_datetime = models.DateTimeField(default=now)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.requestor} -> {self.target_company} ({self.request_type})"