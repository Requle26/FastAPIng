from fastapi import APIRouter
from schemas.user import User

router = APIRouter()

@router.post("/users")
def create_user(user: User):
    return {
        "message": "생성 성공",
        "user": user
    }