from django.db import models
from django.utils.timezone import now

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