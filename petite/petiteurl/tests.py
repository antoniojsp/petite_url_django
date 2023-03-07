from django.test import TestCase
from datetime import datetime, timezone

string = "2023-03-07T16:43"

def convert_to_utc(time: str):
    import pytz
    datetime_object = datetime.strptime(time, '%Y-%m-%dT%H:%M')
    dtime = datetime_object.astimezone(pytz.utc)
    return dtime

print(convert_to_utc(string))