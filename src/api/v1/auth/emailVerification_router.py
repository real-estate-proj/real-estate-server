from fastapi import APIRouter, HTTPException, Depends, status
from schemas.auth.email_verification_schema import EmailVerificationRequestSchema, EmailVerificationResonseSchema, VerificationCodeResponseSchema
from schemas.response import APIResponse
from sqlalchemy.orm import Session
from core.database.session import init_database
from core.security.security import get_current_user
from services.auth.verificationUser import verifyUser, send_verification_email_task


router = APIRouter ()

@router.post ('/verification/',
             status_code=status.HTTP_202_ACCEPTED,
             response_model=APIResponse[EmailVerificationResonseSchema])
async def verify_user (req: EmailVerificationRequestSchema,
                       user = Depends (get_current_user),
                         database: Session = Depends (init_database)):
    
    codeException = HTTPException (
        status_code=status.HTTP_404_NOT_FOUND,
        detail="can not verify user"
    )
    
    invalidUsedCodeException = HTTPException (
        status_code=status.HTTP_403_FORBIDDEN,
        detail="code has been used"
    )
    
    invalidLivenessCodeException = HTTPException (
        status_code=status.HTTP_403_FORBIDDEN,
        detail="code has been expired"
    )

    invalidCodeException = HTTPException (
        status_code=status.HTTP_406_NOT_ACCEPTABLE,
        detail="invalid code"
    )

    verifyUser (user.email, req.code, database,codeException, invalidUsedCodeException, invalidLivenessCodeException, invalidCodeException)

    return APIResponse (
        message="verify successfully",
        data=EmailVerificationResonseSchema (
            email= user.email,
            account_status = "verified"
        )
    )


@router.get ('/verification-code/',
             status_code=status.HTTP_200_OK,
             response_model=APIResponse[VerificationCodeResponseSchema])
async def getVerificationCode (user = Depends (get_current_user),
                               database: Session = Depends (init_database)):
    email = user.email
    name = user.name
    code = await send_verification_email_task (email, name, database)
    return APIResponse (
        message="verfication email has been sent, check your email",
        data=VerificationCodeResponseSchema (
            email=email, 
            code=code
        )
    )