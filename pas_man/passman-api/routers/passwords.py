from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Password
from schemas import PasswordResponse


router = APIRouter(
    prefix="/passwords",
    tags=["Passwords"]
)


@router.get("/", response_model=list[PasswordResponse])
def get_passwords(db: Session = Depends(get_db)):

    passwords = db.query(Password).all()

    return passwords