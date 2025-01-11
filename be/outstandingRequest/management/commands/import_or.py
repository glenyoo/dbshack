from django.core.management.base import BaseCommand, CommandError
from outstandingRequest.models import OutstandingRequest
from companyAccount.models import CompanyAccount


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = [
            (1, 2045, 2032, 287.36, 356, 'Request to purchase Carbon units', 'Approved', 'Buy', '2024-06-06 05:51:53', '2024-07-01 00:00:00'),
            (2, 2032, 2045, 379.88, 279, 'Request to purchase Carbon units', 'Rejected', 'Sell', '2024-06-12 08:52:01', '2024-06-18 07:42:37'),
            (3, 2040, 2042, 198, 284, 'Request to purchase Carbon units', 'Pending', 'Sell', '2024-07-07 02:52:17', '2024-07-07 00:00:00'),
            (4, 2039, 2045, 400, 703, 'As discussed over the phone, request to purchase Carbon credits at $400.', 'Approved', 'Buy', '2024-07-31 02:52:17', '2024-08-01 01:23:23'),
            (5, 2044, 2029, 106, 478, 'Request to purchase Carbon units', 'Rejected', 'Buy', '2024-08-17 05:52:25', '2024-08-18 09:12:39'),
            (6, 2043, 2041, 293.79, 814, 'Excess carbon in 2024.', 'Rejected', 'Sell', '2024-08-21 08:52:32', '2024-09-21 01:59:40'),
            (7, 2037, 2044, 124, 619, 'Request to purchase Carbon units', 'Approved', 'Sell', '2024-08-24 11:52:40', '2024-09-04 12:30:31'),
            (8, 2043, 2042, 203.16, 502, 'Request to purchase Carbon units', 'Pending', 'Buy', '2024-08-24 02:52:48', '2024-08-24 00:00:00'),
            (9, 2037, 2027, 183.48, 968, 'Get more carbon creditssssss', 'Pending', 'Buy', '2024-09-18 05:52:56', '2024-09-18 00:00:00'),
            (10, 2033, 2034, 550, 1080, 'Request to purchase Carbon units', 'Pending', 'Sell', '2024-12-19 08:53:04', '2024-12-19 00:00:00'),
            (12, 2000, 2025, 500.25, 3.5, 'Projected excess carbon credits for 2025', 'Pending', 'Buy', '2025-01-11 09:01:00', '2025-01-11 09:01:02')
        ]
        for vals in data:
            id, companyid,requesterCompanyid, carbonunitprice,carbonquantity,requestreason,requeststatus,requesttype,created,updated= vals
            requestor = CompanyAccount.objects.filter(id=requesterCompanyid).first()
            company = CompanyAccount.objects.filter(id=companyid).first()
            instance = OutstandingRequest(id=id, requestor=requestor, company=company, carbon_unit_price=carbonunitprice,carbon_quantity=carbonquantity, request_reason=requestreason,request_status=requeststatus,request_type=requesttype)
            instance.save()
