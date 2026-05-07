from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import (
    create_user, get_users, update_user, delete_user
)
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.put("/{user_id}", response_model=UserResponse)
def update(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    updated = update_user(db, user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    deleted = delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.get("/protected")
def protected(token: str = Depends(oauth2_scheme)):
    return {"token_received": token}
