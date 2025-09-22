# app/routes/common.py
from fastapi import APIRouter

router = APIRouter(prefix="/common", tags=["Common APIs"])

@router.get("/ping")
def ping():
    return {"message": "Backend is alive 🚀"}
