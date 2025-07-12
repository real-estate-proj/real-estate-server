from fastapi import APIRouter
from .me_router import router as me_router
from .public_router import router as public_router

userRouter = APIRouter (
    prefix="/user",
    tags=["Users"]
)


userRouter.include_router (me_router)
userRouter.include_router (public_router)