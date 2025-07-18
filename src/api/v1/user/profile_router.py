from fastapi import APIRouter, HTTPException, status, Depends, UploadFile, File
from sqlalchemy.orm import Session
from core.database.session import init_database
from schemas.response import APIResponse
from schemas.user.me_shema import userInforResponseSchema
from core.security.security import get_current_user


router = APIRouter (prefix="/me")

@router.get ('/',
             status_code=status.HTTP_200_OK,
             response_model=APIResponse[userInforResponseSchema])
def get_current_user_infor (user=Depends (get_current_user)):
    return APIResponse (
        message="current user information",
        data=userInforResponseSchema (
            id=user.id,
            name=user.name,
            email=user.email,
            phone=user.phone,
            role=user.role,
            avatar_url=user.avatar_url,
            created_at=user.created_at,
            is_verified=user.is_verified
        )
    )

@router.patch ('/',
               status_code=status.HTTP_200_OK,
               response_model=APIResponse[userInforResponseSchema])
def update_user_infor (new_infor, user = Depends (get_current_user)):


    return APIResponse (
        message="current user information",
        data=userInforResponseSchema (
            id=user.id,
            name=user.name,
            email=user.email,
            phone=user.phone,
            role=user.role,
            avatar_url=user.avatar_url,
            created_at=user.created_at,
            is_verified=user.is_verified
        )
    )


@router.delete ('/',
                status_code=status.HTTP_204_NO_CONTENT)
def delete_user (user = Depends (get_current_user)):
    pass


@router.post ('/avatar/',
              status_code=status.HTTP_200_OK,
              response_model=APIResponse)
def upload_avatar (user = Depends (get_current_user),
                   image: UploadFile = File (...),
                   database: Session =Depends (init_database)):
    pass

