from fastapi import APIRouter
from .auth import authRouter

routerV1 = APIRouter ()

routerV1.include_router (authRouter)
