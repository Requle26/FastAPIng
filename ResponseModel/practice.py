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


# ===========================
# 문제 1

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return {
        "name": "김성일",
        "age": 17,
        "password": "1234"
    }

# 사용자가
# GET /users/1
# 을 요청했습니다.

# 1. Response Body에는 무엇이 반환될까요?
# {
#   "name": "김성일",
#   "age": 17,
# }
# 2. password는 응답에 포함될까요?
# 포함 안됌
# 3. Status Code는 무엇일까요?
# 200

# ===========================
# 문제 2

class UserResponse(BaseModel):
    name: str

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return {
        "name": "김성일",
        "age": 17,
        "password": "1234"
    }

# Response Body는 어떻게 될까요?
# {"name": "김성일"}

# ===========================
# 문제 3

# User(BaseModel)의 역할은 무엇일까요?

# A.
# 서버가 클라이언트에게 보내는 데이터의 형식

# B.
# 클라이언트가 서버에 보내는 데이터(Request Body)의 형식

# 정답은?
# B

# ===========================
# 문제 4

# UserResponse(BaseModel)의 역할은 무엇일까요?

# A.
# Request Body

# B.
# Response Body

# 정답은?
# B

# ===========================
# 문제 5

# response_model을 사용하는 가장 큰 이유는 무엇일까요?

# A.
# 요청(Request)을 검사하기 위해

# B.
# 응답(Response)에서 필요한 데이터만 보내기 위해

# C.
# Status Code를 변경하기 위해

# 정답은?
# B

# ===========================
# 문제 6

# 다음 중 response_model에 의해
# 자동으로 제외되는 데이터는?

class UserResponse(BaseModel):
    name: str
    age: int

# return

# {
#     "name": "김성일",
#     "age": 17,
#     "password": "1234",
#     "email": "test@test.com"
# }

# 응답에서 제외되는 데이터는?
# "password": "1234", "email": "test@test.com"

# ===========================
# 문제 7

# 아래 코드의 Status Code는 무엇일까요?

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return {
        "name": "홍길동",
        "age": 25,
        "password": "abcd"
    }

# A.
# 200

# B.
# 201

# C.
# 404

# 정답은?
# A

# ===========================
# 문제 8

# 아래 빈칸을 채워보세요.

# BaseModel은
# 클라이언트가 서버로 보내는 데이터
# 를 정의한다.

# response_model은
# 서버가 클라이언트에게 보내는 데이터
# 를 정의한다.


# ===========================
# 문제 9

# 다음 코드에서

class User(BaseModel):
    name: str
    age: int
    password: str

class UserResponse(BaseModel):
    name: str
    age: int

# 왜 User와 UserResponse를
# 따로 만들까요?

# 자신의 말로 설명해보세요.
# User는 클라이언트가 서버에게 보내는 데이터를 정의함으로써 서버에 password를 전송해 사용자 인증을 진행하고
# UserResponse는 서버가 클라이언트에게 보내는 데이터를 정의해 password를 전송 대상에서 제외시켜 비밀번호를 노출시키지 않는다

# ===========================
# 문제 10 (오늘의 핵심)

# 아래 실행 흐름을 순서대로 적어보세요.

# A.
# response_model이 적용된다.

# B.
# 클라이언트가 GET 요청을 보낸다.

# C.
# 함수가 return을 실행한다.

# D.
# Response Body가 만들어진다.

# 1 -> B
# 2 -> A
# 3 -> D
# 4 -> C