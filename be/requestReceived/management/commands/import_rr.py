from django.core.management.base import BaseCommand, CommandError
from requestReceived.models import RequestReceived
from outstandingRequest.models import OutstandingRequest


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = [
            (1, 1, '2024-06-13 00:00:00', 'Overdue Request 1: You have yet to approve Rodriguez Inc\'s request to Buy 356 units of carbon at $287.36.', 'Viewed', '2024-06-14 00:03:12', '2024-06-06 05:51:53', '2024-07-01 00:00:00'),
            (2, 2, '2024-06-19 00:00:00', 'Overdue Request 2: You have yet to approve Farrell, Collins and Windler\'s request to Sell 279 units of carbon at $379.88.', 'Cancelled', None, '2024-06-12 08:52:01', '2024-06-18 07:42:37'),
            (3, 3, '2024-07-14 00:00:00', 'Overdue Request 3: You have yet to approve Emmerich - Langworth\'s request to Sell 284 units of carbon at $198.', 'Scheduled', None, '2024-07-07 02:52:17', '2024-07-07 00:00:00'),
            (4, 4, '2024-08-07 00:00:00', 'Overdue Request 4: You have yet to approve Farrell, Collins and Windler\'s request to Buy 703 units of carbon at $400.', 'Cancelled', None, '2024-07-31 02:52:17', '2024-08-01 01:23:23'),
            (5, 5, '2024-08-24 00:00:00', 'Overdue Request 5: You have yet to approve Heathcote - Windler\'s request to Buy 478 units of carbon at $106.', 'Cancelled', None, '2024-08-17 05:52:25', '2024-08-18 09:12:39'),
            (6, 6, '2024-08-28 00:00:00', 'Overdue Request 6: You have yet to approve Price - Lemke\'s request to Sell 814 units of carbon at $293.79.', 'Viewed', '2024-08-28 08:01:02', '2024-08-21 08:52:32', '2024-09-21 01:59:40'),
            (7, 7, '2024-08-31 00:00:00', 'Overdue Request 7: You have yet to approve Koelpin LLC\'s request to Sell 619 units of carbon at $124.', 'Viewed', '2024-09-04 12:01:33', '2024-08-24 11:52:40', '2024-09-04 12:30:31'),
            (8, 8, '2024-08-31 00:00:00', 'Overdue Request 8: You have yet to approve Emmerich - Langworth\'s request to Buy 502 units of carbon at $203.16.', 'Scheduled', None, '2024-08-24 02:52:48', '2024-08-24 00:00:00'),
            (9, 9, '2024-09-25 00:00:00', 'Overdue Request 9: You have yet to approve Senger LLC\'s request to Buy 968 units of carbon at $183.48.', 'Scheduled', None, '2024-09-18 05:52:56', '2024-09-18 00:00:00'),
            (10, 10, '2024-12-26 00:00:00', 'Overdue Request 10: You have yet to approve Mills Inc\'s request to Sell 1080 units of carbon at $550.', 'Scheduled', None, '2024-12-19 08:53:04', '2024-12-19 00:00:00'),
            (11, 12, '2025-01-18 00:00:00', 'Overdue Request 12: You have yet to approve TechTrek 2025 Pte Ltd\'s request to Buy 3.5 units of carbon at $500.25.', 'Scheduled', None, '2025-01-11 09:01:00', '2025-01-11 09:01:02')

        ]
        for vals in data:
            id,requestid, alertdatetime,alertext, alertstatus,alertviewdate,create,update = vals
            requestor = OutstandingRequest.objects.filter(id=requestid).first()
            instance = RequestReceived(id=id,request=requestor,alert_datetime=alertdatetime,alert_text=alertext,alert_status=alertstatus,alert_view_date=alertviewdate)
            instance.save()
