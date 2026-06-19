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

# -----------------------
# 문제 1

@app.get("/users")
def get_users():
    return users

# 사용자가 GET /users 를 요청했습니다.

# 1. 어떤 함수가 실행될까요?
# get_users() 함수 실행
# 2. 무엇이 반환될까요?
# users가 반환

# -----------------------
# 문제 2

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return users[user_id]

# 사용자가
# GET /users/2
# 를 요청했습니다.

# # 1. user_id에는 무엇이 들어갈까요?
# user_id에는 Path Parameter가 들어감
# # 2. 반환되는 데이터는?
# users에 user_id인덱스가 반환됌

# -----------------------
# 문제 3

@app.post("/users")
def create_user(user: User):
    new_id = len(users) + 1

    users[new_id] = {
        "name": user.name,
        "age": user.age
    }

    return users[new_id]

# 사용자가

# {
#     "name": "김성일",
#     "age": 17
# }

# 을 보냈습니다.

# 1. Request Body는 무엇일까요?
# {
#     "name": "김성일",
#     "age": 17
# }
# # 2. new_id는 얼마가 될까요?
# users길이에 1을 더한 3이 된다
# # 3. users에는 어떤 데이터가 추가될까요?
# 추가하는 사람의 name과 age데이터가 추가됌

# -----------------------
# 문제 4

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    users[user_id] = {
        "name": user.name,
        "age": user.age
    }

    return users[user_id]

# 사용자가

# PUT /users/1

# {
#     "name": "김철수",
#     "age": 30
# }

# 을 보냈습니다.

# 1. Path Parameter는?
# 1
# 2. Request Body는?
# {
#     "name": "김철수",
#     "age": 30
# }
# 3. users는 어떻게 바뀔까요?
# users = {
#     1: {"name": "김철수", "age": 30},
#     2: {"name": "홍길동", "age": 25}
# }


# -----------------------
# 문제 5

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    del users[user_id]

    return {"message": "삭제 완료"}

# DELETE /users/2

# 요청 후

# users에는 무엇이 남을까요?
# 1: {"name": "김철수", "age": 20} 가 남는다

# -----------------------
# 문제 6

# 다음 중 가장 적절한 HTTP Method를 고르세요.

# A.
#  사용자 전체 조회
# get

#  B.
# 새로운 사용자 생성
# post

#  C.
# 기존 사용자 정보 수정
# put

#  D.
# 사용자 삭제
# delete

# -----------------------
# 문제 7

# 다음 중 Request Body를 사용하는 것은?

# A.
GET /users

# B.
GET /users/3

# C.
POST /users

# D.
DELETE /users/2

# 정답 : C

# -----------------------
# 문제 8 (오늘의 핵심)

# 다음 흐름을 순서대로 적어보세요.

# A.
GET /users

# B.
POST /users

# C.
PUT /users/2

# D.
DELETE /users/1

# 사용자가 회원을

# 1. 생성하고
# 2. 수정하고
# 3. 삭제한 뒤
# 4. 마지막 상태를 확인

# 하려고 합니다.

# 어떤 순서가 가장 자연스러울까요?

# B -> C -> D -> A