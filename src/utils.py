"""This module contains utility functions for the automaticGrindr project."""


def log_message(message):
    print(f'[INFO] {message}')


def random_string(length=10):
    import string
    import random
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))