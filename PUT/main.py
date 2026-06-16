from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id : int
    name : str
    age : int

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {
        "id": user_id,
        "name": user.name,
        "age": user.age
    }

# user_id는 25
# user.name은 "홍길동"
# age는 30

# {
#     "id": 25,
#     "name": "홍길동",
#     "age" : 30
# }

#-----------------------

@app.put("users/{user_id}")
def update_user(user_id: int, user: User):

    return {
        "message": f"{user_id}번 사용자가 수정되었습니다."
    }

# 사용자가
# PUT /users/10

# body
# {
#     "name": "김성일",
#     "age": 18
# }
# 을 보내면

# 응답 JSON은 무엇일까요?

# 정답
# {
#     "message": "10번 사용자가 수정되었습니다."
# }
