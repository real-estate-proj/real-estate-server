from fastapi import HTTPException, status
from crud.auth.emailverification import getVerificationCode, updateCodeStatus
from datetime import datetime
from crud.auth.emailverification import createNewCode, removeExistCode
from crud.user.user import updateUserStatus
from services.email.sendEmail import sendEmail
from schemas.email.emailSchema import EmailSchema
from utils.renderEmailTemplate import render_verification_email
from sqlalchemy.orm import Session


async def send_verification_email_task(email: str, name: str, db: Session):
    try:
        removeExistCode (email, db)
        email_ver = createNewCode(email, db)
        email_data = EmailSchema(
            email=email,
            subject="Verification code for your account",
            content=render_verification_email(
                name=name,
                code=email_ver.code,
                expires_at=email_ver.expires_at,
                templateName="verification_email.html"
            )
        )
        try:
            await sendEmail(email_data)
        except Exception as e:
            raise HTTPException (
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="failed to send the verification email"
            )
        return email_ver.code
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
    