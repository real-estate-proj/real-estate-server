from pydantic import BaseModel, EmailStr


# for got password 
class forgotPasswordRequestSchema (BaseModel):
    email: EmailStr

class forgotPasswordResponseSchema (BaseModel):
    email: EmailStr


# request password
class resetPasswordRequestShema (BaseModel):
    email: EmailStr
    code: str

class resetPasswordResponseSchema (BaseModel):
    email: EmailStr