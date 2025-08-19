
from fastapi import APIRouter, Depends, FastAPI, HTTPException, Query
from sqlmodel import Session

from database import create_db_and_tables, get_session

from models import User
from routes.users import router as user_router
from routes.workout import router as worker_router
from routes.nutrition import router as nutrition_router
from routes.progress import router as progress_router
from routes.chat import router as chat_router


app = FastAPI()

app.include_router(user_router)
app.include_router(worker_router)
app.include_router(nutrition_router)
app.include_router(progress_router)
app.include_router(chat_router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
async def health():
    return { "message" : "live"}

# POST /auth/register - User registration
# POST /auth/login - User login
# GET /auth/user/{user_id} - Get user profile

@app.get("/auth/register")
def register_user(user: User, session: Session = Depends(get_session)):
        session.add(user)
        session.commit()
        session.refresh(user)
        return {
             "message" : "user registered !!",
             "user" : user
        }

@app.get("/auth/login")
def login(userToken: str):
     return {
          "message" : "login successful"
     }

@app.get("/auth/user/{userId}")
def get_user(userId: int, session: Session = Depends(get_session)):
        user = session.get(User, userId)
        return user