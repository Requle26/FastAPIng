# PUT

## PUT이란?
- 기존 데이터를 수정하는 HTTP 메서드이다.

## GET / POST / PUT 차이

GET
- 데이터 조회

POST
- 새로운 데이터 생성

PUT
- 기존 데이터 수정

## PUT 요청 구조

URL
/users/2

Body

{
  "name": "홍길동",
  "age": 30
}

- Path Parameter(user_id): 어떤 데이터를 수정할지
- Request Body: 무엇으로 수정할지

## 수정 흐름

클라이언트
↓
PUT 요청
↓
FastAPI
↓
Path Parameter + BaseModel
↓
수정 대상 찾기
↓
데이터 수정
↓
응답 반환