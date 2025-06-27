from crud.user.user import getUser, createNewUser
from schemas.auth.register_schema import RegisterRequestSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException, BackgroundTasks
from crud.auth.emailverification import createNewCode
from services.email.sendEmail import sendEmail
from schemas.email.emailSchema import EmailSchema
from utils.renderEmailTemplate import render_verification_email


def send_verification_email_task(email: str, name: str, db: Session):
    try:
        email_ver = createNewCode(email, db)
        email_data = EmailSchema(
            email=email,
            subject="Verification code for your account",
            content=render_verification_email(
                name=name,
                code=email_ver.code,
                expires_at=email_ver.expires_at
            )
        )
        import asyncio
        asyncio.run(sendEmail(email_data))
    finally:
        db.close()


def register (user: RegisterRequestSchema, database: Session, exception: HTTPException, background_tasks: BackgroundTasks):
    existing_user = getUser({"email": user.email, "phone": user.phone}, database)

    if existing_user:
        raise exception
    new_user =  createNewUser (user, database)
    background_tasks.add_task(send_verification_email_task, new_user.email, new_user.name, database)

    return new_user
