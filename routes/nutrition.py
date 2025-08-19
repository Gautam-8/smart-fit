
from fastapi import APIRouter, Depends, FastAPI, HTTPException, Query
from sqlmodel import create_engine, SQLModel, Session, select

from database import get_session
from models import Nutrition


router = APIRouter()

@router.post("/nutrition")
def create_nutrition(nutrition: Nutrition, session: Session = Depends(get_session)):
        session.add(nutrition)
        session.commit()
        session.refresh(nutrition)
        return nutrition


@router.get("/nutrition")
def read_nutrition(session: Session = Depends(get_session)):
        nutritions = session.exec(select(Nutrition)).all()
        return nutritions
    

@router.delete('/nutrition')
async def delete_nutrition(nutritionId: int, session: Session = Depends(get_session)):
    nutrition = session.get(Nutrition, nutritionId)
    if not nutrition:
        raise HTTPException(status_code=404, detail="nutrition out not found")
    session.delete(nutrition)
    session.commit()
    return {"ok": True}

