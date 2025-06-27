from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import ExpiredSignatureError, jwt, JWTError
from ..config.env import settings
from sqlalchemy.orm import Session
from core.database.session import init_database
from models.user import RevokedToken, User
import random
import string

oauth2_scheme = OAuth2PasswordBearer (tokenUrl='api/v1/auth/login/')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    MINUTES = settings.access_token_exp_time
    expire = datetime.utcnow() + timedelta (minutes=MINUTES)
    to_encode.update({"exp": expire, "type": "access"})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    MINUTES = settings.refresh_token_exp_time
    expire = datetime.utcnow() + timedelta (minutes=MINUTES)
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

def decode_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        return payload
    except ExpiredSignatureError:
        return None
    except JWTError:
        return None

def generate_verification_code(length=6) -> str:
    return ''.join(random.choices(string.digits, k=length))

def is_revoked (token, db: Session):
    token = db.query (RevokedToken).filter (RevokedToken.access_token == token).first ()
    if not token:
        return False
    return True

def get_current_user (token: str = Depends (oauth2_scheme), db: Session = Depends (init_database)):
    payload = decode_token (token)
    print (payload)
    if not payload:
        raise HTTPException (
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid token"
        )
    if is_revoked (token, db):
        raise HTTPException (
            status_code=status.HTTP_403_FORBIDDEN,
            detail="token has been revoked"
        )
    
    user = db.query (User).filter (User.email == payload["email"]).first ()
    if not user:
        raise HTTPException (
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user not found"
        )
    
    user.pop ("password_hash")
    return user
