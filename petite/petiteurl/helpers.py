from bs4 import BeautifulSoup
from datetime import datetime, timezone
from random import randrange
import requests
from string import ascii_lowercase, digits


def is_expired(exp_date: datetime):
    """
    if exp_date (expiration date) is less than current date (now), then return true
    :param exp_date (datetime aware object
    :return: boolean, true if the page request comes after the expiration date.
    """
    now = datetime.now(timezone.utc)
    return exp_date < now


def generate_hash(length: int) -> str:
    """
    Creates a random hash. For right now, we only allow lowercase letters and digits.
    :param length:  size of the hash we want
    :return: string with random characters [a-z0-9]
    """
    list_characters = ascii_lowercase + digits
    result = ""
    for i in range(length):
        result += list_characters[randrange(0, len(list_characters) - 1)]

    return result


def get_title(url: str) -> str:
    """
    Returns the title of the website to be display in our results.
    :param url: url of the website
    :return: name of the website title
    """
    # TODO polish this more.
    try:
        reqs = requests.get(url)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)

    # using the BeautifulSoup module
    soup = BeautifulSoup(reqs.text, 'html.parser')
    # displaying the title
    return soup.title.string[:30] + "..."
