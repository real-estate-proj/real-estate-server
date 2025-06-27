from sqlalchemy.orm import Session
from typing import Optional
from models.auth import EmailVerification
from schemas.auth.email_verification_schema import EmailVerificationRequestSchema
from core.security.security import generate_verification_code
from datetime import datetime, timedelta
from core.config.env import settings

def createNewCode  (email: str,
                     database: Session, 
                     table=EmailVerification) -> Optional[EmailVerification]:
    code = generate_verification_code ()
    emailVerObject= EmailVerification(
        email=email,
        code=code,
        expires_at=datetime.now() + timedelta(minutes=settings.verification_code_exp_time)
    )
    database.add (emailVerObject)
    database.commit ()
    database.refresh (emailVerObject)
    return emailVerObject

def getVerificationCode (email: str,
                        database: Session,
                         table=EmailVerification):
    emailVerification = database.query (emailVerification).filter (
        emailVerification.email == email
    ).first ()
    return emailVerification