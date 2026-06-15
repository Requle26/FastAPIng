from fastapi import FastAPI

app = FastAPI()

# 문제 1
@app.get("/search")
def search(keyword: str):
    return {"keyword": keyword}

# 사용자가 http://127.0.0.1:8000/search?keyword=fastapi 로 접속했을때

# 1. 어떤 함수가 실행될까요?
# 2. keyword에는 어떤 값이 들어갈까요?
# 3. 반환되는 JSON은 무엇일까요?

# 정답
# 1. search()함수 실행
# 2. keyword에는 fastapi가 들어감 문자열
# 3. 반환되는 JSON은 {"keyword": "fastapi"}

# -----------------------

# 문제 2
@app.get("/products")
def products(category: str):
    return {"category": category}

# 사용자가 http://127.0.0.1:8000/products?category=keyboard 로 접속했을때

# 1. 어떤 함수가 실행될까요?
# 2. category에는 어떤 값이 들어갈까요?
# 3. 반환값은?

# 정답
# 1. products()함수 실행
# 2. category에는 keyboard가 들어감 문자열
# 3. 반환값은 JSON형식으로 {"category": "keyboard"}

# -----------------------

# 문제 3
@app.get("/users")
def users(page: int):
    return {"page": page}

# 사용자가 http://127.0.0.1:8000/users?page=5 로 접속했을때

# 1. page에는 어떤 값이 들어갈까요?
# 2. 왜 Path Parameter가 아니라 Query Parameter를 사용했을까요?

# 정답
# 1. page에는 5가 들어감 정수
# 2. 상품자체를 특정하는것이 아닌 page가 5인것만 특정하기 때문

# -----------------------

# 문제 4
@app.get("/users/{user_id}")
def get_user(user_id: int, detail: bool):
    return {
        "user_id": user_id,
        "detail": detail
    }

# 사용자가 http://127.0.0.1:8000/users/15?detail=true 로 접속했을때

# 1. 어떤 함수가 실행될까요?
# 2. user_id 값은?
# 3. detail 값은?
# 4. 반환 JSON은?

# 정답
# 1. get_user()함수 실행
# 2. user_id값은 15
# 3. detail 값은 true
# 4. 반환 JSON은 {"user_id": 15, "detail": true}

# -----------------------

# 문제 5
@app.get("/posts/{post_id}")
def get_post(post_id: int, comment: bool):
    return {
        "post": post_id,
        "comment": comment
    }

# 사용자가 http://127.0.0.1:8000/posts/99?comment=false 로 접속했을때

# 1. Path Parameter는 무엇일까요?
# 2. Query Parameter는 무엇일까요?
# 3. 반환 JSON은?

# 정답
# 1. Path Parameter는 /posts
# 2. Query Parameter는 /99
# 3. 반환 JSON은 {"post": 99, "comment": false}

# -----------------------

# 문제 6

# 온라인 쇼핑몰입니다.
# 25번 상품을 조회하고,
# 리뷰도 같이 보고 싶습니다.
# 어떤 URL이 가장 적절할까요?

# A
# /products?product_id=25&review=true

# B
# /products/25?review=true

# C
# /25/products?review=true

# 1. 정답은?
# 2. 왜 그렇게 생각했나요?

# 정답
# 1. B
# 2. Query Parameter가 없으면(검색어가 없으면) 상품 전체가 나와야한다고 생각하기에
# products가 Query Parameter로 있는 B 선택

# -----------------------

# 문제 7

# 사용자가 /books/7?detail=true 로 접속하면
# 다음 JSON을 반환해야합니다.

# {
#     "book_id": 7,
#     "detail": true
# }

#정답
@app.get("/books/{book_id}")
def search(book_id: int, detail: bool):
    return {
        "book_id": book_id,
        "detail": detail
    }

# 다 안 맞을수 있음

# Path Parameter와
# Query Parameter의 차이 더 공부하기