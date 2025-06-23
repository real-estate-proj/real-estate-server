from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Literal

class RefreshTokenRequestShema (BaseModel):
    refresh_token: str

class LoginResponseSchema (BaseModel):
    access_token: str
    refresh_token: str