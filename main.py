
from fastapi import FastAPI

from database import create_db_and_tables

from routes.users import router as user_router
from routes.workout import router as worker_router
from routes.nutrition import router as nutrition_router
from routes.progress import router as progress_router

app = FastAPI()

app.include_router(user_router)
app.include_router(worker_router)
app.include_router(nutrition_router)
app.include_router(progress_router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
async def health():
    return { "message" : "live"}
