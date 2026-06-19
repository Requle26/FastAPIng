from fastapi import FastAPI

app = FastAPI()

users = {
    1: {"name": "김철수", "age": 20},
    2: {"name": "홍길동", "age": 25},
    3: {"name": "이순신", "age": 30}
}

# -----------------------
# 문제 1

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    del users[user_id]
    return {"message": "삭제 완료"}

# 사용자가
# DELETE /users/2
# 를 요청했습니다.

# 1. user_id에는 어떤 값이 들어갈까요?
# 2. 실제 실행되는 del 코드는 무엇일까요?
# 3. users에는 어떤 데이터가 남을까요?

# -----------------------
# 문제 2

users = {
    10: {"name": "김성일"},
    20: {"name": "홍길동"}
}

# 다음 코드의 결과는?

# 10 in users
# 30 in users
# 20 not in users

# -----------------------
# 문제 3

users = {
    1: {"name": "김철수"},
    2: {"name": "홍길동"}
}

# 다음 코드의 출력은?

if 3 not in users:
    print("사용자가 없습니다.")

# -----------------------
# 문제 4

users = {
    1: {"name": "김철수"},
    2: {"name": "홍길동"}
}

# 왜 아래 코드가 필요한지 설명해보세요.

# if user_id not in users:
#     return {"error": "사용자가 존재하지 않습니다."}

# -----------------------
# 문제 5 (종합)

# 현재 users

users = {
    1: {"name": "김철수"},
    2: {"name": "홍길동"},
    3: {"name": "이순신"}
}

# 사용자가

# DELETE /users/3

# 을 요청했습니다.

# 삭제 후 users는 어떻게 될까요?