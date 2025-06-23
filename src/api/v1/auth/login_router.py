from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from core.database.session import init_database
from core.security.security import verify_password, create_access_token, create_refresh_token, decode_token
from schemas.auth.login_schema import LoginResponseSchema, RefreshTokenRequestShema
from schemas.response import APIResponse
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from crud.user.user import getUser


router = APIRouter ()

@router.post ('/login/',
              status_code=status.HTTP_200_OK,
              response_model=APIResponse[LoginResponseSchema])
async def login (user_credentials: OAuth2PasswordRequestForm = Depends (),
                 database: Session = Depends (init_database)):
    user  = getUser ({"email": user_credentials.username}, database)
    if not user:
        raise HTTPException (
            status_code=status.HTTP_403_FORBIDDEN,
            detail="invalid credentials"
        )
    
    if not verify_password (user_credentials.password, user.password_hash):
        raise HTTPException (
            status_code=status.HTTP_403_FORBIDDEN,
            detail="invalid password"
        )
    
    acessToken = create_access_token ({
        "id": user.id,
        "email": user.email,
        "name": user.name,
        "role": user.role,
        "is_verified": user.is_verified
    })

    refreshToken = create_refresh_token ({
        "id": user.id,
        "email": user.email,
        "name": user.name,
        "role": user.role,
        "is_verified": user.is_verified
    }

    )
    return APIResponse(
        status_code=status.HTTP_201_CREATED,
        message="Login successfully",
        data=LoginResponseSchema(
            access_token=acessToken,
            refresh_token=refreshToken
        )   
    )


@router.post ('/refresh/',
              status_code=status.HTTP_200_OK,
              response_model=APIResponse[LoginResponseSchema])
async def refresh_token (token: RefreshTokenRequestShema):
    user_data = decode_token (token.refresh_token)
    acessToken = create_access_token ({
        **user_data
    })

    refreshToken = create_refresh_token ({
        **user_data
    }

    )
    return APIResponse(
        status_code=status.HTTP_201_CREATED,
        message="Refresh successfully",
        data=LoginResponseSchema(
            access_token=acessToken,
            refresh_token=refreshToken
        )   
    )


@router.post ('/logout/',
              status_code=status.HTTP_200_OK)
async def logout ():
    pass