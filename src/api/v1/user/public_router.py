from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from core.database.session import init_database
from schemas.response import APIResponse
from core.security.security import get_current_user

router = APIRouter ()

@router.get ('/',
             status_code=status.HTTP_200_OK,
             response_model=APIResponse)
def get_all_user ():
    pass


@router.get ('/{id}',
             status_code=status.HTTP_200_OK,
             response_model=APIResponse)
def get_user_infor (database: Session = Depends (init_database)):
    pass


@router.get ('/landlords/',
             status_code=status.HTTP_200_OK,
             response_model=APIResponse)
def get_all_landlords ():
    pass


@router.get ('/tenants/',
             status_code=status.HTTP_200_OK,
             response_model=APIResponse)
def get_all_tenants ():
    pass


@router.get ('/{id}/properties/',
             status_code=status.HTTP_200_OK,
             response_model=APIResponse)
def get_user_properties (user=Depends (get_current_user)):
    pass

@router.get ('/{id}/blogs/',
             status_code=status.HTTP_200_OK,
             response_model=APIResponse)
def get_user_blogs (user=Depends (get_current_user)):
    pass


