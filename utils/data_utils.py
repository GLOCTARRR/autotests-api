import random
import string
import time


def generate_email() -> str:
    return f"test.{time.time()}@exampl.com"


def generate_string(length: int = 10):
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(length)
    )
