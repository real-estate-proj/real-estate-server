from fastapi import APIRoute, APIRouter

userRouter = APIRouter (
    prefix="/user",
    tags=["Users"]
)