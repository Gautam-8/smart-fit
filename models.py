# Users: id, username, email, password, age, weight, height, goals

from sqlalchemy import table
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    age: int
    weight: int 
    height: int
    goals: str

# Workouts: id, user_id, plan_name, date, exercises, duration

class Workout(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int
    plan_name: str
    date: str
    exercises: str
    duration: str

# Nutrition: id, user_id, date, meals, calories, macros
class Nutrition(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int
    date: str
    meals: str
    calories: str
    macros: str


# Progress: id, user_id, workout_id, sets, reps, weights, notes
class Progress(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int
    workout_id: str
    sets: str
    reps: str
    weights: str
    notes: str