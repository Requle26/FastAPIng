from fastapi import FastAPI, HTTPException

app = FastAPI()

users = {
    1: {"name": "김철수"},
    2: {"name": "홍길동"}
}

# ===========================
# 문제 1

@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="사용자를 찾을 수 없습니다."
        )

    return users[user_id]

# 사용자가
# GET /users/2
# 를 요청했습니다.

# 1. user_id에는 무엇이 들어갈까요?
# 2가 들어간다
# 2. if문의 결과는?
# False
# 3. raise는 실행될까요?
# 실행되지 않는데
# 4. return은 무엇을 반환할까요?
# {2: {"name": "홍길동"}}
# 5. Status Code는?
# 200

# ===========================
# 문제 2

@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="사용자를 찾을 수 없습니다."
        )

    return users[user_id]

# 사용자가
# GET /users/100
# 를 요청했습니다.

# 1. user_id에는?
# 100이다
# 2. if문의 결과는?
# True
# 3. raise는 실행될까요?
# 실행된다
# 4. return은 실행될까요?
# 실행되지 않는다
# 5. Status Code는?
# 404
# 6. Response Body는?
# {detail:"사용자를 찾을 수 없습니다."}

# ===========================
# 문제 3

# raise HTTPException()을 사용하는 이유는 무엇일까요?

# 1.
# return으로도 가능하다.

# 2.
# FastAPI에게 오류가 발생했음을 알려주기 위해 사용한다.

# 3.
# JSON을 만들기 위해 사용한다.

# 정답은?
# 2번

# ===========================
# 문제 4

# 다음 중 정상 응답을 보내는 코드는?

# A.
# return users[user_id]

# B.
# raise HTTPException(
#     status_code=404,
#     detail="사용자를 찾을 수 없습니다."
# )

# 정답은?
# A

# ===========================
# 문제 5

# 다음 중 오류 응답을 보내는 코드는?

# A.
# return users[user_id]

# B.
# raise HTTPException(
#     status_code=404,
#     detail="사용자를 찾을 수 없습니다."
# )

# 정답은?
# B

# ===========================
# 문제 6

# 다음 중 가장 적절한 Status Code는?

# 사용자가 존재하지 않습니다.

# GET /users/50

# A.
# 200

# B.
# 201

# C.
# 400

# D.
# 404

# 왜 그렇게 생각하나요?
# D, 404가 존재하지 않는 데이터에 접근했을때 뜨는 코드라서

# ===========================
# 문제 7

# 아래 코드에서

if 100 not in users:
    pass

# if문의 결과는?

# True
# False

# 왜 그렇게 생각하나요?
# True, 100이 users에 없으면인데 users에 key값은 1, 2밖에 없다

# ===========================
# 문제 8 (오늘의 핵심)

# 아래 실행 순서를 번호로 적어보세요.

# A.
# return users[user_id]

# B.
# user_id에 100이 들어간다.

# C.
# raise HTTPException()

# D.
# if user_id not in users 확인

# GET /users/100 요청이 들어왔습니다.

# 1 -> B
# 2 -> D
# 3 -> C
# 4 -> A


# ===========================
# 문제 9 (응용)

# 아래 코드에서

@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="사용자를 찾을 수 없습니다."
        )

    return users[user_id]

# GET /users/2 요청이 들어왔습니다.

# return과 raise 중
# 실제로 실행되는 것은 무엇인가요?
# return
# 왜 그렇게 생각하나요?
# users에 2라는 key가 있기때문에 user_id not in users가 false가 되서 raise가 아닌 return 이 실행된다

# ===========================
# 문제 10 (오늘의 최종 정리)

# 아래 빈칸을 채워보세요.

# 정상적인 데이터를 반환할 때는
# return 를 사용한다.

# 오류를 반환할 때는
# raise 를 사용한다.

# 존재하지 않는 데이터를 요청하면
# Status Code는 404 이다.

# HTTPException은
# 오류를 알리기 위해 사용한다.