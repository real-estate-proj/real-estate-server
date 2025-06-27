from sqlalchemy.orm import Session
from typing import Optional
from models.auth import EmailVerification
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
    emailVerification = database.query (EmailVerification).filter (
        EmailVerification.email == email
    ).first ()
    return emailVerification

def updateCodeStatus(email: str, database: Session):
    instance = database.query(EmailVerification).filter(EmailVerification.email == email).first()
    
    if not instance:
        return None  
    
    instance.is_used = True
    database.commit()
    database.refresh(instance)
    return instance


def removeExistCode (email, database):
    rc = database.query (EmailVerification).filter (EmailVerification.email == email).first ()
    if rc:
        database.delete (rc)
        database.commit ()
        return True
    return False