# DELETE

## DELETE란?

- 기존 데이터를 삭제하는 HTTP 메서드이다.

## DELETE 요청 구조

URL
/users/2

- Path Parameter(user_id): 어떤 데이터를 삭제할지 지정한다.
- Request Body는 보통 사용하지 않는다.

## 삭제 과정

클라이언트
↓
DELETE 요청
↓
FastAPI
↓
Path Parameter(user_id)
↓
삭제할 데이터 찾기
↓
del users[user_id]
↓
응답 반환

## 예외 처리

삭제하려는 데이터가 없을 수도 있다.

```python
if user_id not in users:
    return {"error": "사용자가 존재하지 않습니다."}