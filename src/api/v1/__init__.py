from fastapi import APIRouter
from .auth.register_router import route

routerV1 = APIRouter ()

routerV1.include_router (route)
