from crud.auth.emailverification import getVerificationCode, updateCodeStatus
from datetime import datetime
from crud.auth.emailverification import createNewCode
from crud.user.user import updateUserStatus
from services.email.sendEmail import sendEmail
from schemas.email.emailSchema import EmailSchema
from utils.renderEmailTemplate import render_verification_email
from sqlalchemy.orm import Session


async def send_verification_email_task(email: str, name: str, db: Session):
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
        await sendEmail(email_data)
    finally:
        db.close()


def verifyUser (email, sentCode, db, codeException, invalidUsedCodeException, invalidLivenessCodeException, invalidCodeException):
    emailVerification = getVerificationCode (email, db)

    if not emailVerification:
        raise codeException
    
    if emailVerification.is_used:
        raise invalidUsedCodeException
    
    if emailVerification.code != sentCode:
        raise invalidCodeException
    
    if emailVerification.expires_at < datetime.utcnow ():
        raise invalidLivenessCodeException


    updateCodeStatus (email, db)
    updateUserStatus (email, True, db)
    