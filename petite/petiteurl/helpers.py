from string import ascii_lowercase, digits
from random import randrange
from datetime import datetime, timezone
import requests
from bs4 import BeautifulSoup

def convert_to_utc(time: str):
    datetime_object = datetime.strptime(time, '%Y-%m-%dT%H:%M')
    return datetime_object.astimezone(timezone.utc)


def generate_hash(length: int) -> str:
    list_characters = ascii_lowercase + digits
    result = ""
    for i in range(length):
        result += list_characters[randrange(0, len(list_characters) - 1)]

    return result

def get_title(url:str):
    # making requests instance
    reqs = requests.get(url)
    # using the BeautifulSoup module
    soup = BeautifulSoup(reqs.text, 'html.parser')
    # displaying the title
    return soup.title.string[:20] + "..."

def compare_dates(date):
    pass

