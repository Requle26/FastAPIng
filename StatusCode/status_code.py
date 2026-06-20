from fastapi import FastAPI, status

app = FastAPI()

@app.get("/users")
def get_users():
    return {
        "message": "조회 성공"
    }

@app.post(
    "/users",
    status_code=status.HTTP_201_CREATED
)
def create_user():
    return {
        "message": "생성 성공"
    }

@app.put("/users/1")
def update_user():
    return {
        "message": "수정 성공"
    }

@app.delete("/users/1")
def delete_user():
    return {
        "message": "삭제 성공"
    }