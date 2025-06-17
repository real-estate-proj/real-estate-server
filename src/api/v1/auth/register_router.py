from fastapi import APIRouter, HTTPException, Depends, status
from schemas.auth.register_schema import RegisterRequestSchema, RegisterResponseSchema
from schemas.response import APIResponse
from sqlalchemy.orm import Session
from database.session import init_database
# from models.user import User
from crud.user.user import getUser, createNewUser


route = APIRouter(
    tags=["Registration"],
    prefix="/user"
)

@route.post('/register',
            status_code=status.HTTP_201_CREATED,
            response_model=APIResponse[RegisterResponseSchema])
async def create_new_user(user: RegisterRequestSchema,
                        database: Session = Depends(init_database)
):
    existing_user = getUser({"email": user.email, "phone": user.phone}, database)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email hoặc số điện thoại đã tồn tại."
        )

    new_user =  createNewUser (user, database)
    return APIResponse(
        status_code=status.HTTP_201_CREATED,
        message="Tạo tài khoản thành công",
        data=RegisterResponseSchema(
            name=new_user.name,
            email=new_user.email,
            phone=new_user.phone,
            role=new_user.role,
            avatar_url=new_user.avatar_url,
            created_at=new_user.created_at
        )
    )

@route.post ('/activate',
             status_code=status.HTTP_202_ACCEPTED)
async def activate_user (user,
                         database: Session = Depends (init_database)):
    pass
    

@route.get ('/testing')
def test ():
    return {
        "no content"
    }
