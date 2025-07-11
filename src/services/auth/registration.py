from crud.user.user import getUser, createNewUser
from schemas.auth.register_schema import RegisterRequestSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException, BackgroundTasks
from .verificationUser import send_verification_email_task



def register (user: RegisterRequestSchema, database: Session, exception: HTTPException, background_tasks: BackgroundTasks):
    existing_user = getUser({"email": user.email, "phone": user.phone}, database)

    if existing_user:
        raise exception
    new_user =  createNewUser (user, database)
    background_tasks.add_task(send_verification_email_task, new_user.email, new_user.name, "verification_email.html", database)

    return new_user
