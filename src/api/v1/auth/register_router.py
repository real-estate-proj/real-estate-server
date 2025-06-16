from fastapi import APIRouter, HTTPException, Depends, status
from schemas.auth.register_schema import RegisterRequestSchema, RegisterResponseSchema
from schemas.response import APIResponse
from sqlalchemy.orm import Session
from sqlalchemy import or_
from database.session import init_database
from models.user import User
from core.security.security import hash_password

route = APIRouter(
    tags=["registration"],
    prefix="/user"
)

@route.post('/register',
            status_code=status.HTTP_201_CREATED,
            response_model=APIResponse[RegisterResponseSchema])
async def create_new_user(
                        user: RegisterRequestSchema,
                        database: Session = Depends(init_database)
):
    existing_user = database.query(User).filter(
        or_(
            User.email == user.email,
            User.phone == user.phone
        )
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email hoặc số điện thoại đã tồn tại."
        )

    hashed_pwd = hash_password(user.password)

    new_user = User(
        name=user.name,
        email=user.email,
        phone=user.phone,
        password_hash=hashed_pwd,
        role=user.role,
        avatar_url=user.avatar_url,
        created_at=user.created_at
    )

    database.add(new_user)
    database.commit()
    database.refresh(new_user)

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
