from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Literal

class RegisterRequestSchema(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str
    role: Literal['landlord', 'tenant'] 
    avatar_url: str = ""
    created_at: datetime = Field(default_factory=datetime.utcnow)


class RegisterResponseSchema(BaseModel):
    name: str
    email: EmailStr
    phone: str
    role: Literal['landlord', 'tenant'] 
    avatar_url: str = ""
    created_at: datetime
    is_verified: bool
