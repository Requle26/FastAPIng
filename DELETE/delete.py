from fastapi import FastAPI

app = FastAPI()

users = {
    1: {"name": "김철수", "age": 20},
    2: {"name": "홍길동", "age": 25},
    3: {"name": "이순신", "age": 30}
}

@app.delete("/users/{user_id}")
def delete_user(user_id: Int):
    del users[user_id]

    return {
        "message": f"{user_id}번 사용자가 삭제되었습니다."
    }