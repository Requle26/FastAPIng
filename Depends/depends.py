from fastapi import FastAPI, Depends

app = FastAPI()

def check_login():
    print("로그인 검사 실행!")
    return "김성일"

@app.get("/users")
def get_users(login=Depends(check_login)):
    return {
        "message": "조회 성공",
        "login": login
    }