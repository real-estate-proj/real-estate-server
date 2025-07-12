from pydantic import BaseModel, EmailStr
from datetime import datetime


class userInforRequestSchema (BaseModel):
    pass


class userInforResponseSchema (BaseModel):
    name: str
    email: EmailStr
    phone: str
    role:str 
    avatar_url: str = ""
    created_at: datetime
    is_verified: bool