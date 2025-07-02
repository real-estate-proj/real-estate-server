from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from core.database.session import init_database
from schemas.auth.login_schema import LoginResponseSchema, RefreshTokenRequestShema, AccessTokenResponseSchema
from schemas.response import APIResponse
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from services.auth.login import loginUser, refreshToken
from services.auth.logout import signout
from core.security.security import get_current_user, oauth2_scheme


router = APIRouter ()

@router.post ('/login/',
              status_code=status.HTTP_200_OK,
              response_model=LoginResponseSchema,
              description="Sigining in the user to the app")
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

    return LoginResponseSchema (
        access_token=data["accesstoken"],
        refresh_token=data["refreshtoken"],
        token_type="bearer"
    )


@router.post ('/refresh-token/',
              status_code=status.HTTP_200_OK,
              response_model=APIResponse[AccessTokenResponseSchema])
async def refresh_token (token: RefreshTokenRequestShema):
    exception = HTTPException (
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid token"
    )
    data = refreshToken (token, exception)

    return APIResponse(
        message="refresh successfully",
        data=AccessTokenResponseSchema(
            access_token=data["accesstoken"],
            token_type='bearer'
        )   
    )


@router.post ('/logout/',
              status_code=status.HTTP_200_OK)
async def logout (refresh: RefreshTokenRequestShema,
                    access: str = Depends (oauth2_scheme),
                    user = Depends (get_current_user),
                    database: Session = Depends (init_database)):
    exception = HTTPException (
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="the request must include either an access token or a refresh token"
    )

    userException = HTTPException (
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="refresh token is not belong to the current user"
    )

    tokenException = HTTPException (
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="invalid token"
    )
    signout (access, refresh.refresh_token, database, exception, tokenException, userException, user)
    return {"success"}
