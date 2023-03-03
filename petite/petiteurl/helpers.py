from string import ascii_lowercase, digits
from random import randrange
from datetime import datetime, timezone
from .models import Urls


def convert_to_utc(time: str):
    datetime_object = datetime.strptime(time, '%Y-%m-%dT%H:%M')
    return datetime_object.astimezone(timezone.utc)


def generate_hash(length: int) -> str:
    list_characters = ascii_lowercase + digits
    result = ""
    for i in range(length):
        result += list_characters[randrange(0, len(list_characters) - 1)]

    return result

def compare_dates(date):
    pass