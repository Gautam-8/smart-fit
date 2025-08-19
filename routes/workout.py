
from fastapi import APIRouter, Depends, FastAPI, HTTPException, Query
from sqlmodel import create_engine, SQLModel, Session, select

from database import get_session
from models import Workout


router = APIRouter()

@router.post("/workout")
def create_workout(workOut: Workout, session: Session = Depends(get_session)):
        session.add(workOut)
        session.commit()
        session.refresh(workOut)
        return workOut


@router.get("/workout")
def read_workout(session: Session = Depends(get_session)):
        Workouts = session.exec(select(Workout)).all()
        return Workouts
    

@router.delete('/workout')
async def delete_workout(workoutid: int, session: Session = Depends(get_session)):
    workout = session.get(Workout, workoutid)
    if not workout:
        raise HTTPException(status_code=404, detail="work out not found")
    session.delete(workout)
    session.commit()
    return {"ok": True}

