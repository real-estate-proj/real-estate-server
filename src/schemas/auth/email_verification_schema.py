from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Literal, Text

class EmailVerificationRequestSchema (BaseModel):
    code: str

class EmailVerificationResonseSchema (BaseModel):
    email: EmailStr
    account_status: str

class VerificationCodeResponseSchema (BaseModel):
    email: EmailStr
    code: str
    