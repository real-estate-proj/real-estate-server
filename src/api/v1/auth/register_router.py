from fastapi import APIRouter, HTTPException, Depends, status
from schemas.auth.register_schema import RegisterRequestSchema, RegisterResponseSchema
from schemas.response import APIResponse
from sqlalchemy.orm import Session
from database.session import init_database
# from models.user import User
from crud.user.user import getUser, createNewUser
from services.auth.register import register


router = APIRouter(
    tags=["Registration"],
    prefix="/user"
)

@router.post('/register',
            status_code=status.HTTP_201_CREATED,
            response_model=APIResponse[RegisterResponseSchema])
async def create_new_user(user: RegisterRequestSchema,
                        database: Session = Depends(init_database)
):
    exception = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email hoặc số điện thoại đã tồn tại."
        )
    new_user = register (user, database, exception)
    return APIResponse(
        status_code=status.HTTP_201_CREATED,
        message="Tạo tài khoản thành công",
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

@router.post ('/verification',
             status_code=status.HTTP_202_ACCEPTED)
async def activate_user (user,
                         database: Session = Depends (init_database)):
    pass
    

@router.get ('/testing')
def test ():
    return {
        "no content"
    }
