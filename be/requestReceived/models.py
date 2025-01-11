from django.db import models
from django.utils.timezone import now
from outstandingRequest.models import OutstandingRequest

# RequestReceived model
class RequestReceived(models.Model):
    request = models.ForeignKey(OutstandingRequest, on_delete=models.CASCADE, related_name='alerts')
    alertDatetime = models.DateTimeField()
    alertText = models.TextField()
    alertStatus = models.CharField(max_length=50)
    alertViewDate = models.DateTimeField(null=True, blank=True)
    createdDatetime = models.DateTimeField(default=now)
    updatedDatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Alert for Request ID {self.request.id}"