from fastapi import APIRouter
from .auth import authRouter
from .user import userRouter

routerV1 = APIRouter ()

routerV1.include_router (authRouter)
routerV1.include_router (userRouter)
