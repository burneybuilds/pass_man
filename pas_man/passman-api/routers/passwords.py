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


@router.get("/{requested_password}", response_model=PasswordResponse)
def get_password(requested_password: str, db: Session = Depends(get_db)):
    """Fetches a password record from the database using the requested service name.
    Returns the matching record if found, or a 404 error if the service does not exist.
    """
    password = (
        db.query(Password)
        .filter(Password.service == requested_password)
        .first()
    )

    if password is None:
        raise HTTPException(
            status_code=404,
            detail="Password service not found"
        )

    return password