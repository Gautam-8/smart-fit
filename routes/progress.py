
from fastapi import APIRouter, Depends, FastAPI, HTTPException, Query
from sqlmodel import create_engine, SQLModel, Session, select

from database import get_session
from models import Progress


router = APIRouter()

@router.post("/progress")
def create_progress(progress: Progress, session: Session = Depends(get_session)):
        session.add(progress)
        session.commit()
        session.refresh(progress)
        return progress


@router.get("/progress")
def read_progress(session: Session = Depends(get_session)):
        progresss = session.exec(select(Progress)).all()
        return progresss
    

@router.delete('/progress')
async def delete_progress(progressId: int, session: Session = Depends(get_session)):
    progress = session.get(progress, progressId)
    if not progress:
        raise HTTPException(status_code=404, detail="progress out not found")
    session.delete(progress)
    session.commit()
    return {"ok": True}

