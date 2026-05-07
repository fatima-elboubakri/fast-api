from fastapi import FastAPI
from app.api import auth
from app.schemas.user import UserCreate
from app.api.users import router as user_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}


app.include_router(auth.router, tags=["auth"])
app.include_router(user_router, prefix="/users", tags=["users"])