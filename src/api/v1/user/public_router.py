from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from core.database.session import init_database
from schemas.response import APIResponse
from core.security.security import get_current_user

router = APIRouter ()

@router.get ('/',
             status_code=status.HTTP_200_OK,
             response_model=APIResponse)
def getAllUser ():
    pass


@router.get ('/landlords/',
             status_code=status.HTTP_200_OK,
             response_model=APIResponse)
def getAllLandlords ():
    pass


@router.get ('/tenant/',
             status_code=status.HTTP_200_OK,
             response_model=APIResponse)
def getAllLandlords ():
    pass