# Path Parameter
# /users/123
# 여기서
# 123
# 이 값이 Path Parameter이다

# FastAPI에서는

# @app.get("/users/{user_id}")
# def get_user(user_id : Int):
#     return {"id": user_id}

# 처럼 받음

# -----------------------

# Query Parameter
# /search?keyword=python
# 여기서
# ?keyword=python
# 이 부분이 Query Parameter이다

# 여기서
# keyword -> 변수 이름
# python -> 값

# -----------------------

# 아래 코드를 보고 답해보자
from fastapi import FastAPI

app = FastAPI()

@app.get("/search")
def search(keyword: str):
    return {"keyword": keyword}

# 사용자가 http://127.0.0.1:8000/search?keyword=fastapi로 접속했습니다.


# 1. 어떤 함수가 실행될까요?
# 2. keyword에는 어떤 값이 들어갈까요?
# 3. 반환되는 JSON은 무엇일까요?

# 정답:
# 1. search함수
# 2. fastapi
# 3. {"keyword": fastapi}

# -----------------------

# Query Parameter가 2개일때

@app.get("/search")
def search(keyword: str, page: int):
    return {
        "keyword": keyword,
        "page": page
    }

# 사용자가 http://127.0.0.1:8000/search?keyword=python&page=3 로 접속했습니다.

# 1. 어떤 함수가 실행될까요?
# 2. keyword에는 무엇이 들어갈까요?
# 3. page에는 무엇이 들어갈까요?
# 4. 반환되는 JSON은 무엇일까요?

# 정답
# 1. /search 함수
# 2. python
# 3. 3
# 4. {"keyword": "python", "page": 3}

# -----------------------

# 응용문제

@app.get("/users/{user_id}")
def get_user(user_id: int, detail: bool):
    return {
        "user_id": user_id,
        "detail": detail
    }

# 사용자가 http://127.0.0.1:8000/users/7?detail=true 로 접속했습니다.

# 7은 어디로 들어갈까요?
# true는 어디로 들어갈까요?

# 정답
# 7은 {user_id}로 들어감
# true는 detail에 들어감
