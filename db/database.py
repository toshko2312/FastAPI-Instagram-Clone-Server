from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from db.password import password

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://root:{password}@host.docker.internal/fastapi_instagram_clone"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
