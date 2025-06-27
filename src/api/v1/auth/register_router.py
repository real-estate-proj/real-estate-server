from fastapi import APIRouter, HTTPException, Depends, status, BackgroundTasks
from schemas.auth.register_schema import RegisterRequestSchema, RegisterResponseSchema
from schemas.response import APIResponse
from sqlalchemy.orm import Session
from core.database.session import init_database
from core.security.security import get_current_user
from services.auth.register import register

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
             status_code=status.HTTP_202_ACCEPTED)
async def verify_user (user = Depends (get_current_user),
                         database: Session = Depends (init_database)):
    pass
    

