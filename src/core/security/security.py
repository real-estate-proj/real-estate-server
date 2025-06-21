from passlib.context import CryptContext
from datetime import datetime, timedelta
from ..config.env import settings
from jose import jwt
import random
import string


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password (plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token (data: dict):
    pass

def generate_verification_code(length=6) -> str:
    return ''.join(random.choices(string.digits, k=length))