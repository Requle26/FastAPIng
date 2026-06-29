from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from DATABASE.models import Base

DATABASE_URL = "sqlite:///./DATABASE/users.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base.metadata.create_all(bind=engine)

print("테이블 생성 완료!")