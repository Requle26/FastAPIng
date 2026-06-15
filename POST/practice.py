# 문제 1

# 다음중 POST를 사용하는 가장 적절한 상황은?

# A.
# 상품 목록 조회

# B.
# 회원 가입

# C.
# 게시글 조회

# D.
# 사용자 검색

# 정답
# B, 회원가입은 url로 노출되면 안되는 비밀번호가 있고 가입 정보가 많으면 url이 길어진다

# ---------------------------
# 문제 2

# 다음 요청이 들어왔습니다.
# {
#     "name": "김성일",
#     "age": 17
# }

# 이 데이터는

# 1. URL
# 2. Path Parameter
# 3. Query Parameter
# 4. Request Body

# 중 어디에 들어있는 데이터 일까요?

# 정답
# 4번

# ---------------------------
# 문제 3

# from pydantic import BaseModel

# class User(BaseModel):
#     name: str
#     age: int

# 사용자가

# {
#     "name": "김성일",
#     "age": 17
# }
# 을 보내면

# FastAPI 내부에서는 어떤 객체가 만들어질까요?

# 정답
# user객체?

# ---------------------------
# 문제 4

# @app.post("/users")
# def create_user(user: User):
#     return {
#         "name": user.name,
#         "age": user.age
#     }

# 왜

# user.name

# 을 사용할 수 있을까요?

# 정답
# user가 객체기 때문

# ---------------------------
# 문제 5
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class User(BaseModel):
#     name: str
#     age: int

# @app.post("/users")
# def create_user(user: User):
#     return {
#         "message": f"{user.name}님 환영합니다.",
#         "next_age": user.age + 1
#     }

# 사용자가

# {
#     "name": "김성일",
#     "age": 17
# }
# 을 보내면 응답 JSON은?

# 정답
# {
#     "message": f"{user.name}님 환영합니다.",
#     "next_age": user.age + 1
# }

# ---------------------------
# 문제 6

# 다음 요청을 보냈습니다.

# {
#     "name": "김성일",
#     "age": "열일곱"
# }

# 어떤 일이 일어날까요?
# 1. 함수가 실행된다.
# 2. FastAPI가 BaseModel 검사 후 에러를 반환한다.
# 3. age가 자동으로 17이 된다.

# 잘 모르겠다..
# 2번인건 알겠는데

# ---------------------------
# 문제 7

# 다음 코드를 완성하세요

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Product(BaseModel):
#     name: str
#     price: int

# @app.post("/products")
# def create_product(product: Product):
#     return {
#         "name": product.name,
#         "price": product.price
#     }

# 사용자는

# {
#     "name": "키보드",
#     "price": 50000
# }

# 를 보낼 예정입니다.

# 빈칸을 채워보세요.

# ---------------------------
# 문제 8

# 다음 흐름을 순서대로 번호를 매겨보세요.

# A. FastAPI가 BaseModel로 데이터를 검사한다.
# B. create_user() 함수가 실행된다.
# C. 브라우저가 JSON을 보낸다.
# D. User 객체가 생성된다.

# 예를 들어

# 1 -> A
# 2 -> B

# 처럼 적으면 됩니다.

# 정답
# 1 -> C
# 2 -> A
# 3 -> D
# 4 -> B


# 문제 다 맞는지 확인할것