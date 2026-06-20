Exception

Exception은 프로그램 실행 중 발생하는 오류를 의미한다.

FastAPI에서는 HTTPException을 사용하여 클라이언트에게 오류와 상태 코드를 전달할 수 있다.

⸻

HTTPException

HTTP 오류를 발생시키는 클래스이다.

사용자가 존재하지 않거나 요청한 데이터를 찾을 수 없을 때 많이 사용한다.

예시

raise HTTPException(
    status_code=404,
    detail="사용자를 찾을 수 없습니다."
)

⸻

raise

예외를 발생시키고 함수를 즉시 종료한다.

raise가 실행되면 아래 코드는 실행되지 않는다.

예시

if user_id not in users:
    raise HTTPException(
        status_code=404,
        detail="사용자를 찾을 수 없습니다."
    )
return users[user_id]

위 코드에서 사용자가 존재하지 않으면 return은 실행되지 않는다.

⸻

return

정상적인 데이터를 반환할 때 사용한다.

예시

return users[user_id]

응답

* 200 OK
* 사용자 정보 반환

⸻

404 Not Found

요청한 데이터를 찾을 수 없을 때 사용한다.

예시

GET /users/100

응답

{
    "detail": "사용자를 찾을 수 없습니다."
}

⸻

return과 raise의 차이

return

* 정상적인 데이터를 반환한다.
* 함수가 정상적으로 종료된다.

raise

* 오류를 발생시킨다.
* 함수가 즉시 종료된다.
* 아래 코드는 실행되지 않는다.

⸻

기억하기

return → 정상 데이터 반환

raise → 오류 발생

HTTPException → 오류를 클라이언트에게 전달

404 → 요청한 데이터를 찾을 수 없음

detail → 오류의 원인을 설명하는 메시지