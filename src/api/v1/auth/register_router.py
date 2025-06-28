from fastapi import APIRouter, HTTPException, Depends, status, BackgroundTasks
from schemas.auth.register_schema import RegisterRequestSchema, RegisterResponseSchema
from schemas.auth.email_verification_schema import EmailVerificationRequestSchema, EmailVerificationResonseSchema, VerificationCodeResponseSchema
from schemas.response import APIResponse
from sqlalchemy.orm import Session
from core.database.session import init_database
from core.security.security import get_current_user
from services.auth.register import register
from services.auth.verificationUser import verifyUser, send_verification_email_task

router = APIRouter()

@router.post('/register/',
            response_model=APIResponse[RegisterResponseSchema])
async def create_new_user(user: RegisterRequestSchema,
                        background_tasks: BackgroundTasks,
                        database: Session = Depends(init_database)
):
    exception = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or phone number has been used by another user"
        )
    
    new_user = register (user, database, exception, background_tasks)
    return APIResponse(
        message="create account successfully, please check the email and verify the account within 30 minutes since you receives the email",
        data=RegisterResponseSchema(
            name=new_user.name,
            email=new_user.email,
            phone=new_user.phone,
            role=new_user.role,
            avatar_url=new_user.avatar_url,
            created_at=new_user.created_at,
            is_verified=new_user.is_verified
        )
    )


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