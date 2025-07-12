from fastapi import APIRouter, HTTPException, status, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from core.database.session import init_database
from schemas.response import APIResponse
from services.auth.password import getRecoveryCode, resetUserPassword

from schemas.auth.password_schema import forgotPasswordRequestSchema, forgotPasswordResponseSchema, resetPasswordRequestShema, resetPasswordResponseSchema
router = APIRouter ()


@router.get ('/forgot-password/',
              status_code=status.HTTP_200_OK,
              response_model=APIResponse[forgotPasswordResponseSchema])
async def forgotPassword (request: forgotPasswordRequestSchema,
                          backgroud_tasks: BackgroundTasks,
                          database: Session = Depends (init_database)):
    exception = HTTPException (
        status_code=status.HTTP_404_NOT_FOUND,
        detail="user not found"
    )
    getRecoveryCode (request.email, exception, database, backgroud_tasks)
    return APIResponse (
        message="Reset password verification code has been sent, check your email",
        data = forgotPasswordResponseSchema (
            email=request.email
        )
    )


@router.post ('/reset-password/',
              status_code=status.HTTP_200_OK,
              response_model=APIResponse[resetPasswordResponseSchema])
def resetPassword (request: resetPasswordRequestShema,
                   database: Session = Depends  (init_database)):
    
    userException = HTTPException (
        status_code=status.HTTP_404_NOT_FOUND,
        detail="user not found"
    )
    
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

    resetUserPassword (request.email, request.code, request.new_password, database,
                       userException, codeException, invalidCodeException, invalidLivenessCodeException, invalidUsedCodeException)
    
    return APIResponse (
        message="Reset password successfully, please login again",
        data = resetPasswordResponseSchema (
            email=request.email
        )
    )

