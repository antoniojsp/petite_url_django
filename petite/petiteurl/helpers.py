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

    if not exp_date:  # if None, no expiration date was set up.
        return False

    now = datetime.now(timezone.utc)
    return exp_date < now


def is_valid_hash(hash_val: str, length: int) -> bool:
    """
    Checks if all the characters in the custom hash are valid. Only valid is lower case and digits (at the moment)
    Checks if the length of the hash is valid
    :param length: valid length of the hash
    :param hash_val: string with the custom hash
    :return: boolean, true if it's valid false if it has one invalid character
    """

    valid_characters = ascii_lowercase + digits

    for char in hash_val:
        if char not in valid_characters:
            return False

    if len(hash_val) != length:
        return False

    return True


def generate_hash(length: int) -> str:
    """
    Creates a random hash. For right now, we only allow lowercase letters and digits.
    :param length:  size of the hash we want
    :return: string with random characters [a-z0-9]
    """
    valid_characters = ascii_lowercase + digits
    random_hash = ""
    for i in range(length):
        random_hash += valid_characters[randrange(0, len(valid_characters) - 1)]

    return random_hash


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
