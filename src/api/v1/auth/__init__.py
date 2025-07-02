from fastapi import APIRouter
from .authentication_router import router as authentication_routes
from .registration_router import router as register_routes
from .emailVerification_router import router as emailVerification_routes
from .password_router import router as password_routes

authRouter = APIRouter (
    prefix="/auth",
    tags=["Authencation"],
)


authRouter.include_router (register_routes)
authRouter.include_router (authentication_routes)
authRouter.include_router (emailVerification_routes)
authRouter.include_router (password_routes)