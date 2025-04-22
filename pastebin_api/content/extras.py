import secrets
import string

from .models import Content


def generate_random_token(length=10):
    characters = string.ascii_letters + string.digits
    while True:
        token = ''.join(secrets.choice(characters) for _ in range(length))
        if not Content.objects.filter(token=token).exists():
            return token