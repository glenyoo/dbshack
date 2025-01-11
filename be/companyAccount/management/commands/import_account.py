from django.core.management.base import BaseCommand, CommandError
from companyAccount.models import CompanyAccount


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = [
            (1, 'Kemmer, Cronin and Walter', 0, 2147, 547973, '2023-02-10 00:00:00', '2024-11-18 00:00:00'),
            (2000, 'TTTTTTTTTTTTTechtrek is here', 1, 9999, 2026000, '2025-01-11 10:00:00', '2025-01-11 10:00:00'),
            (2025, 'TechTrek 2025 Pte Ltd', 1, 200, 150000, '2025-01-11 09:00:00', '2025-01-11 09:00:00'),
            (2027, 'Senger LLC', 1, 648, 959359, '2024-08-30 00:00:00', '2024-11-19 00:00:00'),
            (2028, 'Conn - DuBuque', 0, 295, 164535, '2023-03-18 00:00:00', '2023-12-14 00:00:00'),
            (2029, 'Heathcote - Windler', 1, 8124, 139228, '2024-04-25 00:00:00', '2024-12-28 00:00:00'),
            (2030, 'Hand - Ledner', 0, 9032, 650415, '2024-11-08 00:00:00', '2024-11-15 00:00:00'),
            (2031, 'MacGyver Group', 0, 3036, 524802, '2023-10-14 00:00:00', '2024-12-22 00:00:00'),
            (2032, 'Rodriguez Inc', 1, 6784, 897333, '2023-02-18 00:00:00', '2024-07-01 00:00:00'),
            (2033, 'Gleason LLC', 1, 1764, 657636, '2023-01-13 00:00:00', '2024-12-28 00:00:00'),
            (2034, 'Mills Inc', 1, 7867, 370155, '2023-08-29 00:00:00', '2024-09-02 00:00:00'),
            (2035, 'Mayer, Haley and Stiedemann', 0, 958, 759482, '2024-10-19 00:00:00', '2024-11-08 00:00:00'),
            (2036, 'Gutmann - Langosh', 0, 161, 165937, '2024-09-07 00:00:00', '2024-11-21 00:00:00'),
            (2037, 'Hansen - Daugherty', 1, 3434, 56068, '2024-04-30 00:00:00', '2024-09-06 00:00:00'),
            (2038, 'Sanford - Bruen', 0, 541, 201799, '2024-06-29 00:00:00', '2024-03-05 00:00:00'),
            (2039, 'Haag and Sons', 1, 1118, 252659, '2024-03-01 00:00:00', '2025-01-07 17:49:43'),
            (2040, 'Hermiston, Hettinger and Streich', 1, 7492, 849960, '2023-04-09 00:00:00', '2024-09-23 00:00:00'),
            (2041, 'Price - Lemke', 1, 2043, 419981, '2023-07-26 00:00:00', '2024-12-10 00:00:00'),
            (2042, 'Emmerich - Langworth', 1, 7116, 742714, '2024-01-29 00:00:00', '2024-09-30 00:00:00'),
            (2043, 'Abbott - Hane', 1, 4419, 487599, '2024-07-04 00:00:00', '2024-08-11 00:00:00'),
            (2044, 'Koelpin LLC', 1, 4708, 509389, '2024-04-12 00:00:00', '2024-09-06 00:00:00'),
            (2045, 'Farrell, Collins and Windler', 1, 1252, 277831, '2023-07-21 00:00:00', '2024-08-01 00:00:00')
        ]
        for vals in data:
            id, companyName, activeAccount, carbonBalance, cashBalance, created, updated = vals
            instance = CompanyAccount(id=id, company_name=companyName,carbon_balance=carbonBalance,cash_balance=cashBalance,active_account=activeAccount)
            instance.save()