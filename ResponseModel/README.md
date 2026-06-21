Response Model

Response Model은 서버가 클라이언트에게 어떤 데이터를 보낼지 정의하는 기능이다.

필요한 데이터만 응답하고, 민감한 데이터는 응답에서 제외할 수 있다.

⸻

User

User는 클라이언트가 서버로 보내는 데이터(Request Body)의 형태를 정의한다.

예시

class User(BaseModel):
    name: str
    age: int
    password: str

회원가입처럼 서버가 데이터를 받을 때 사용한다.

⸻

UserResponse

UserResponse는 서버가 클라이언트에게 보내는 데이터(Response Body)의 형태를 정의한다.

예시

class UserResponse(BaseModel):
    name: str
    age: int

비밀번호와 같이 응답에 포함하면 안 되는 데이터는 정의하지 않는다.

⸻

response_model

response_model은 응답(Response)의 형태를 지정하는 옵션이다.

예시

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return {
        "name": "김성일",
        "age": 17,
        "password": "1234"
    }

위 코드에서 함수는 password까지 반환하지만,

class UserResponse(BaseModel):
    name: str
    age: int

만 정의되어 있으므로 실제 응답은

{
    "name": "김성일",
    "age": 17
}

만 반환된다.

⸻

BaseModel

BaseModel은 데이터의 형태(구조)를 정의하는 클래스이다.

사용하는 위치에 따라 역할이 달라진다.

* User → Request Body
* UserResponse → Response Body

⸻

Request Body와 Response Body

Request Body

* 클라이언트가 서버로 보내는 데이터
* User(BaseModel)를 사용한다.

Response Body

* 서버가 클라이언트에게 보내는 데이터
* UserResponse(BaseModel)와 response_model을 사용한다.

⸻

Response Model을 사용하는 이유

* 필요한 데이터만 응답할 수 있다.
* 비밀번호와 같은 민감한 정보를 숨길 수 있다.
* 응답 형식을 일정하게 유지할 수 있다.

⸻

기억하기

* BaseModel은 데이터의 형태를 정의한다.
* User는 서버가 받는 데이터(Request Body)이다.
* UserResponse는 서버가 보내는 데이터(Response Body)이다.
* response_model은 UserResponse에 정의된 필드만 응답한다.
* Response Model을 사용하면 password, email 등의 민감한 정보를 자동으로 제외할 수 있다.