from fastapi import APIRouter, HTTPException, status, Depends


router = APIRouter (
    tags=["Auth"],
    prefix="/auth"
)

