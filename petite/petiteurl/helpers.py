from string import ascii_lowercase, digits
from random import randrange
from datetime import datetime, timezone


def convert_to_utc(time: str):
    datetime_object = datetime.strptime(time, '%Y-%m-%dT%H:%M')
    return datetime_object.astimezone(timezone.utc)



def generate_hash(length: int)->str:
    list_characters = ascii_lowercase + digits
    result = ""
    for i in range(length):
        result += list_characters[randrange(0, len(list_characters) - 1)]

    return result


import datetime

date_time_str = '2022-12-01 10:27:03.929149'
date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)