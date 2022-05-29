from random import choice
from string import digits, ascii_letters


def get_random_string(size):
    return ''.join(choice(digits + ascii_letters) for i in range(size))
