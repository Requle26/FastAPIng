from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    password: str

class UserResponse(BaseModel):
    name: str
    age: int

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return {
        "name": "김성일",
        "age": 17,
        "password": "1234"
    }