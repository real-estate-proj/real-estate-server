from fastapi import APIRouter
from .profile_router import router as profile_router
from .public_router import router as public_router

userRouter = APIRouter (
    prefix="/user",
    tags=["Users"]
)


userRouter.include_router (profile_router)
userRouter.include_router (public_router)