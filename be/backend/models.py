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

# OutstandingRequest model
class OutstandingRequest(models.Model):
    REQUEST_TYPES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    ]
    requestor = models.ForeignKey(CompanyAccount, on_delete=models.CASCADE, related_name='requests_made')
    target_company = models.ForeignKey(CompanyAccount, on_delete=models.CASCADE, related_name='requests_received')
    carbon_unit_price = models.FloatField(default=0)
    carbon_quantity = models.FloatField(default=0)
    request_reason = models.TextField()
    request_status = models.CharField(max_length=50, default='Pending Approval')
    request_type = models.CharField(max_length=4, choices=REQUEST_TYPES)
    created_datetime = models.DateTimeField(default=now)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.requestor} -> {self.target_company} ({self.request_type})"
    
# RequestReceived model
class RequestReceived(models.Model):
    request = models.ForeignKey(OutstandingRequest, on_delete=models.CASCADE, related_name='alerts')
    alert_datetime = models.DateTimeField()
    alert_text = models.TextField()
    alert_status = models.CharField(max_length=50)
    alert_view_date = models.DateTimeField(null=True, blank=True)
    created_datetime = models.DateTimeField(default=now)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Alert for Request ID {self.request.id}"