from crud.user.user import getUser, createNewUser
from schemas.auth.register_schema import RegisterRequestSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException, BackgroundTasks
from crud.user.emailverification import createNewCode
from services.email.sendEmail import sendEmail
from schemas.email.emailSchema import EmailSchema
from utils.renderEmailTemplate import render_verification_email


def register (user: RegisterRequestSchema, database: Session, exception: HTTPException, background_tasks: BackgroundTasks):
    existing_user = getUser({"email": user.email, "phone": user.phone}, database)

    if existing_user:
        raise exception
    new_user =  createNewUser (user, database)

    emailVerObject = createNewCode (new_user.email, database)
    email = EmailSchema(
        email=new_user.email,
        subject="Verification code for your account",
        content=render_verification_email (
            name=new_user.name,
            code=emailVerObject.code,
            expires_at=emailVerObject.expires_at
        )
    )
    background_tasks.add_task (sendEmail, email)
    return new_user
