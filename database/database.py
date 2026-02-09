from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from .config import settings

engine = create_engine(
    url=settings.DATABASE_URL,
    echo=settings.sqlalchemy_echo,
    pool_size=5,
    max_overflow=10,
)

new_session = sessionmaker(bind=engine, expire_on_commit=False)





