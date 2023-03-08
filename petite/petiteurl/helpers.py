from bs4 import BeautifulSoup
import datetime
from datetime import datetime
from random import randrange
import requests
from string import ascii_lowercase, digits


def generate_hash(length: int) -> str:
    list_characters = ascii_lowercase + digits
    result = ""
    for i in range(length):
        result += list_characters[randrange(0, len(list_characters) - 1)]

    return result


def get_title(url: str) -> str:
    # making requests instance
    reqs = requests.get(url)
    # using the BeautifulSoup module
    soup = BeautifulSoup(reqs.text, 'html.parser')
    # displaying the title
    return soup.title.string[:30] + "..."
