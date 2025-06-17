from fastapi import APIRouter, HTTPException, status, Depends


route = APIRouter (
    tags=["Auth"],
    prefix="/auth"
)

