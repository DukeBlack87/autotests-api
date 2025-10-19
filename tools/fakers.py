import time
from faker import Faker

def get_random_email() -> str:
    return f"test.{time.time()}@example.com"

def name_generator() -> str:
    return Faker().name()

def last_name_generator() -> str:
    return Faker().last_name()

def first_name_generator() -> str:
    return Faker().first_name()

def password_generator() -> str:
    return Faker().password()