from crud.user.user import getUser, createNewUser
from schemas.auth.register_schema import RegisterRequestSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException

def register (user: RegisterRequestSchema, database: Session, exception: HTTPException):
    existing_user = getUser({"email": user.email, "phone": user.phone}, database)

    if existing_user:
        raise exception
    new_user =  createNewUser (user, database)
    return new_user
