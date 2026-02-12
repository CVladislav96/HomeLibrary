from pydantic import BaseModel, ConfigDict

from models.book import StatusBook


class BookBase(BaseModel):
    title: str
    author: str
    description: str | None = None
    published_year: int | None = None
    status: StatusBook | None = None


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookRead(BookBase):
    id: int
    status: StatusBook
    model_config = ConfigDict(from_attributes=True)
