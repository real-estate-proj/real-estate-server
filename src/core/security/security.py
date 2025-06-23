from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from ..config.env import settings
import random
import string

oauth2_scheme = OAuth2PasswordBearer (tokenUrl='auth/login')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now() + timedelta(days=settings.access_token_exp_time | 2) 
    to_encode.update({"exp": expire, "type": "access"})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now() + timedelta(days=settings.refresh_token_exp_time | 7)
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

def decode_token(token: str) -> dict | None:
    try:
        return jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
    except JWTError:
        return None

def generate_verification_code(length=6) -> str:
    return ''.join(random.choices(string.digits, k=length))


def get_current_user  (token: str = Depends (oauth2_scheme)):
    user_infor = decode_token (token=token)

if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
    print (sys.path)
    token = create_access_token({"name": "minhtuan", "id": 123})
    print("Access Token:", token)

    refresh = create_refresh_token({"name": "minhtuan", "id": 123})
    print("Refresh Token:", refresh)
