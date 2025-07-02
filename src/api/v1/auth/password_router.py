from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from core.database.session import init_database
from schemas.response import APIResponse
from core.security.security import get_current_user

from schemas.auth.password_schema import forgotPasswordRequestSchema, forgotPasswordResponseSchema, resetPasswordRequestShema, resetPasswordResponseSchema
router = APIRouter ()


@router.post ('/forgot-password/',
              status_code=status.HTTP_200_OK,
              response_model=APIResponse[forgotPasswordResponseSchema])
async def forgotPassword (request: forgotPasswordRequestSchema,
                          database: Session = Depends (init_database)):
    
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
    pass

