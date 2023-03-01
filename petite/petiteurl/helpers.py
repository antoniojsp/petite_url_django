from string import ascii_lowercase, digits
from random import randrange


def generate_hash(length:int):
    characters = ascii_lowercase + digits
    result = ""
    for i in range(length):
        result += characters[randrange(0, len(characters)-1)]

    return  result