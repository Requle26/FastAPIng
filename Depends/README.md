Depends

Depends는 FastAPI에서 공통 기능을 여러 API에서 재사용하기 위한 기능이다.

요청이 들어올 때마다 지정한 함수를 먼저 실행하고, 그 반환값을 API 함수에 전달한다.

⸻

기본 사용법

from fastapi import Depends
def check_login():
    return "김성일"
@app.get("/users")
def get_users(login=Depends(check_login)):
    return {
        "user": login
    }

위 코드에서 FastAPI는 요청이 들어오면 먼저 check_login()을 실행한다.

반환값인 "김성일"을 login 변수에 저장한 뒤 get_users()를 실행한다.

⸻

실행 순서

1. 클라이언트가 요청을 보낸다.
2. Depends에 등록된 함수가 실행된다.
3. 반환값이 함수의 매개변수에 전달된다.
4. API 함수가 실행된다.
5. Response Body가 반환된다.

⸻

Depends를 사용하는 이유

같은 기능을 여러 API에서 반복해서 작성하지 않기 위해 사용한다.

예를 들어

* 로그인 확인
* 관리자 권한 확인
* 데이터베이스 연결

과 같은 공통 기능을 하나의 함수로 만들어 여러 API에서 재사용할 수 있다.

⸻

check_login()과 Depends의 차이

일반 함수 호출

login = check_login()

직접 함수를 호출하는 방식이다.

Depends 사용

login = Depends(check_login)

FastAPI가 요청이 들어올 때마다 check_login()을 자동으로 실행하고, 반환값을 전달해 준다.

⸻

예시

def check_login():
    return "홍길동"
@app.get("/users")
def get_users(login=Depends(check_login)):
    return {
        "user": login
    }

응답

{
    "user": "홍길동"
}

⸻

기억하기

* Depends는 공통 기능을 재사용하기 위한 기능이다.
* 요청이 들어올 때마다 지정한 함수를 자동으로 실행한다.
* 함수의 반환값을 매개변수로 전달한다.
* 로그인 확인, 권한 검사, 데이터베이스 연결 등에 자주 사용된다.