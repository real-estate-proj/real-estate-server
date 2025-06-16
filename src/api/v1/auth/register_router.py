from fastapi import APIRouter, HTTPException, Depends, status
from schemas.auth.register_schema import RegisterRequestSchema, RegisterResponseSchema
from sqlalchemy.orm import Session
from database.session import init_database

router = APIRouter (tags="registration")


@router.post ('/register', 
              status_code=status.HTTP_201_CREATED, 
              response_model=RegisterResponseSchema)
async def create_new_user (user: RegisterRequestSchema, 
                           database: Session = Depends (init_database)):
    pass
    