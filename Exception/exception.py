from fastapi import FastAPI, HTTPException

app = FastAPI()

users = {
    1: {"name": "김철수"},
    2: {"name": "홍길동"}
}

@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id not in users:
        raise HTTPException( # raise는 함수를 중단하고 에러를 발생시킨다
            status_code=404,
            detail="사용자를 찾을 수 없습니다."
        )
    return users[user_id]