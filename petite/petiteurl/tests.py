from django.test import TestCase
from datetime import datetime, timezone

import datetime
from datetime import datetime
from django.utils import timezone
now = timezone.now()
# date in yyyy/mm/dd format
# d1 = datetime.datetime(2018, 5, 3)
# d2 = datetime.datetime(2018, 6, 1)
#
# # Comparing the dates will return
# # either True or False
# print("d1 is greater than d2 : ", d1 > d2)
# print("d1 is less than d2 : ", d1 < d2)
# print("d1 is not equal to d2 : ", d1 != d2)
print("2023-03-08 03:06:00+00:00"[:-6])
date1 = datetime.strptime("2023-03-08 03:06:00+00:00"[:-6], '%Y-%m-%d %H:%M:%S')
print(date1<now)