from fastapi import FastAPI, Depends

app = FastAPI()


def check_login():
    return "김성일"


# ===========================
# 문제 1

@app.get("/users")
def get_users(login=Depends(check_login)):
    return {
        "message": "조회 성공",
        "login": login
    }

# 사용자가
# GET /users
# 를 요청했습니다.

# 1. check_login()의 반환값은?
# "김성일"
# 2. login 변수에는 무엇이 들어갈까요?
# "김성일"
# 3. Response Body는 어떻게 될까요?
# {
#   "message": "조회 성공",
#   "login": login
# }
# 4. Status Code는 무엇일까요?
# 200


# ===========================
# 문제 2

def check_login():
    return "홍길동"

@app.get("/users")
def get_users(login=Depends(check_login)):
    return {
        "user": login
    }

# Response Body는 어떻게 될까요?
#     return {
#         "user": "홍길동"
#     }

# ===========================
# 문제 3

# Depends(check_login)의 역할은 무엇일까요?

# A.
# check_login()을 삭제한다.

# B.
# 요청이 들어올 때 check_login()을 실행하고
# 반환값을 함수에 전달한다.

# C.
# Status Code를 변경한다.

# 정답은?
# B


# ===========================
# 문제 4

# check_login()이

def check_login():
    print("로그인 검사")
    return "김성일"

# GET /users를
# 3번 요청했습니다.

# print는 몇 번 실행될까요?

# A.
# 1번

# B.
# 2번

# C.
# 3번

# 정답은?
# C

# ===========================
# 문제 5

# Depends를 사용하는 가장 큰 이유는 무엇일까요?

# A.
# 같은 코드를 여러 API에서 재사용하기 위해

# B.
# Status Code를 바꾸기 위해

# C.
# Response Body를 만들기 위해

# 정답은?
# A

# ===========================
# 문제 6

@app.get("/users")
def get_users(login=Depends(check_login)):
    return {
        "login": login
    }

# 아래 코드에서

# login에는 무엇이 들어갈까요?
# check_login의 반환값이 들어감
# _______________________


# ===========================
# 문제 7

# 다음 중 Depends를 사용할 수 있는 기능은?

# A.
# 로그인 확인

# B.
# 관리자 권한 확인

# C.
# 데이터베이스 연결

# D.
# 위 모두

# 정답은?
# D

# ===========================
# 문제 8

# 아래 빈칸을 채워보세요.

# Depends는
# 같은 코드를 여러 API에서 재사용
# 을(를) 위한 기능이다.

# 요청이 들어올 때마다
# 특정 함수
# 을(를) 실행한다.


# ===========================
# 문제 9

# 왜

# login = check_login()

# 대신

# login = Depends(check_login)

# 를 사용할까요?

# 자신의 말로 설명해보세요.
# Depends는 요청이 들어올 때마다 FastAPI가 자동으로 함수를 실행해 주기 때문에 사용한다.

# ===========================
# 문제 10 (오늘의 핵심)

# 아래 실행 순서를 적어보세요.

# A.
# get_users()가 실행된다.

# B.
# check_login()이 실행된다.

# C.
# 클라이언트가 GET 요청을 보낸다.

# D.
# Response Body가 반환된다.

# 1 -> C
# 2 -> B
# 3 -> A
# 4 -> D