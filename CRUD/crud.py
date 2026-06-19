from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

users = {
    1: {"name": "김철수", "age": 20},
    2: {"name": "홍길동", "age": 25}
}

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return users[user_id]

@app.post("/users")
def create_user(user: User):
    new_id = len(users) + 1

    users[new_id] = {
        "name": user.name,
        "age": user.age
    }

    return {
        "id": new_id,
        "name": user.name,
        "age": user.age
    }

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    users[user_id] = {
        "name": user.name,
        "age" : user.age
    }
    return users[user_id]

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    del users[user_id]
    return {
        "message": "삭제 완료"
    }