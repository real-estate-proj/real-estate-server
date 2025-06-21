from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Literal

class EmailVerificationRequestSchema (BaseModel):
    email: EmailStr
    code: str

class EmailVerificationResonseSchema (BaseModel):
    email: EmailStr
    expires_at: datetime
    is_used: bool = Field (defaul=False)
    