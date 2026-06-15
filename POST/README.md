# FastAPI POST & Request Body 학습

## 1. 오늘 배운 핵심 개념

### POST란?
POST는 서버에 **새로운 데이터를 생성(등록) 요청**하는 HTTP 메서드이다.

- 데이터를 서버에 "보내서 저장"하거나 "처리"할 때 사용한다.
- URL에 데이터가 노출되지 않고, Body에 담겨 전송된다.

---

### Request Body란?
Request Body는 클라이언트가 서버로 보내는 **JSON 데이터 영역**이다.

예:
```json
{
  "name": "김성일",
  "age": 17
}