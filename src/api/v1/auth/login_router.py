from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from core.database.session import init_database
from schemas.auth.login_schema import LoginResponseSchema, RefreshTokenRequestShema, AccessTokenResponseSchema
from schemas.response import APIResponse
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from services.auth.login import loginUser, refreshToken
from core.security.security import get_current_user


router = APIRouter ()

@router.post ('/login/',
              status_code=status.HTTP_200_OK,
              response_model=APIResponse[LoginResponseSchema])
async def login (user_credentials: OAuth2PasswordRequestForm = Depends (),
                 database: Session = Depends (init_database)):
    userException = HTTPException (
        status_code=status.HTTP_403_FORBIDDEN,
        detail="invalid credentials"
    )

    passwordException = HTTPException (
        status_code=status.HTTP_403_FORBIDDEN,
        detail="invalid password"
    )
    
    data = loginUser (user_credentials.username, user_credentials.password, database, userException, passwordException)

    return APIResponse(
        status_code=status.HTTP_200_OK,
        message="Login successfully",
        data=LoginResponseSchema(
            access_token=data["accesstoken"],
            refresh_token=data["refreshtoken"],
            token_type='bearer'
        )   
    )


@router.post ('/refresh/',
              status_code=status.HTTP_200_OK,
              response_model=APIResponse[AccessTokenResponseSchema])
async def refresh_token (token: RefreshTokenRequestShema):
    exception = HTTPException (
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid token"
    )
    data = refreshToken (token, exception)

    return APIResponse(
        status_code=status.HTTP_200_OK,
        message="refresh successfully",
        data=AccessTokenResponseSchema(
            access_token=data["accesstoken"],
            token_type='bearer'
        )   
    )


@router.post ('/logout/',
              status_code=status.HTTP_200_OK)
async def logout ():
    pass


@router.get ('/protected-router/')
def get (user = Depends (get_current_user)):
    return user