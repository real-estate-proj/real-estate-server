from .verificationUser import send_verification_email_task
from fastapi import BackgroundTasks
from crud.user.user import getUser, updateUserPassword
from crud.auth.emailverification import getVerificationCode, updateCodeStatus

from datetime import datetime

def getRecoveryCode (email, exception, db, backgroud_tasks: BackgroundTasks):
    user = getUser ({'email': email}, db)
    if not user:
        raise exception
    backgroud_tasks.add_task (send_verification_email_task, email, user.name, 'passwordreset_email.html', db)


def verifyRecoveryCode (email, sentCode, db, codeException, invalidUsedCodeException, invalidLivenessCodeException, invalidCodeException):
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


def resetUserPassword (email, code, new_password, db, userException, codeException, invalidUsedCodeException, invalidLivenessCodeException, invalidCodeException):
    verifyRecoveryCode (email, code, db, codeException, invalidUsedCodeException, invalidLivenessCodeException, invalidCodeException)
    if not updateUserPassword (email, new_password, db):
        raise userException
    return True