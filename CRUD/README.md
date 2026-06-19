# CRUD

CRUD는 데이터를 관리하는 기본 기능이다.

## GET

- 데이터를 조회한다.
- 데이터를 변경하지 않는다.

예시

GET /users
GET /users/1

---

## POST

- 새로운 데이터를 생성한다.
- Request Body를 사용한다.

예시

POST /users

---

## PUT

- 기존 데이터를 수정한다.
- Path Parameter로 수정할 대상을 찾는다.
- Request Body로 수정할 내용을 받는다.

예시

PUT /users/1

---

## DELETE

- 기존 데이터를 삭제한다.
- 삭제할 대상을 Path Parameter로 받는다.

예시

DELETE /users/1

---

## CRUD 정리

GET    → 조회(Read)

POST   → 생성(Create)

PUT    → 수정(Update)

DELETE → 삭제(Delete)

---

## 기억할 내용

- Path Parameter = 어떤 대상을 처리할지
- Request Body = 어떤 내용으로 처리할지
- GET은 조회
- POST는 생성
- PUT은 수정
- DELETE는 삭제