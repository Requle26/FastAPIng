# 문제 1
@app.get("/")
def home():
    return {"page": "home"}

# 사용자가 어느 주소로 접속해야 home()이 실행될까요?
# 정답 : /

#--------------------------------

# 문제 2

@app.get("/users")
def get_users():
    return ["kim", "lee"]

# 사용자가 http://127.0.0.1:8000/users로 접속하면 어떤 함수가 실행될까요?
# 정답 : get_users

#--------------------------------

# 문제 3

@app.get("/posts")
def get_posts():
    return ["게시글1", "게시글2"]

@app.get("/users")
def get_users():
    return ["kim", "lee"]

# 사용자가 http://127.0.0.1:8000/posts로 접속하면 어떤 함수가 실행될까요?
# 정답 : get_posts

#--------------------------------

# 문제 4

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}

# 사용자가 http://127.0.0.1:8000/users/123로 접속했습니다
# 1. 어떤 함수가 실행될까?
# 2. user_id에는 어떤 값이 들어갈까?
# 3. 반환값은 무엇일까?

# 정답 :
# 1. get_user
# 2. int
# 3. {"id": 123}

#--------------------------------

# 문제 5 (조금 어려움)

@app.get("/")
def home():
    return {"page": "home"}

@app.get("/about")
def about():
    return {"page": "about"}

# 사용자가 http://127.0.0.1:8000/about로 접속했습니다

# 왜 home()이 아니라 about()이 실행될까요?

#정답 : /about으로 get요청을 전송해서