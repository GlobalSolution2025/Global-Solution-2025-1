from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user import UserCreate, UserOut
from app.crud.user import create_user

router = APIRouter()

@router.post("/users/", response_model=UserOut)
def create_user_view(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)
