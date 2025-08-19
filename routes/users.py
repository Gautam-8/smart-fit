
from fastapi import APIRouter, Depends, FastAPI, HTTPException, Query
from sqlmodel import create_engine, SQLModel, Session, select

from database import get_session
from models import User


router = APIRouter()

@router.post("/users")
def create_user(user: User, session: Session = Depends(get_session)):
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


@router.get("/users")
def read_users(session: Session = Depends(get_session)):
        heroes = session.exec(select(User)).all()
        return heroes
    

@router.delete('/users')
async def delete_user(userId: int, session: Session = Depends(get_session)):
    user = session.get(User, userId)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"ok": True}

