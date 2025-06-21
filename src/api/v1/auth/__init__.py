from fastapi import APIRouter
from .login_router import router as login_routes
from .register_router import router as register_routes

authRouter = APIRouter (
    prefix="/auth",
    tags=["Authencation"],
)


authRouter.include_router (register_routes)
authRouter.include_router (login_routes)