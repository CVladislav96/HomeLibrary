from pydantic import BaseModel, ConfigDict
from typing import Optional
from models.book import StatusBook


class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    published_year: Optional[int] = None
    status: Optional[StatusBook] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass
    

class BookRead(BookBase):
    id: int
    status: StatusBook
    model_config = ConfigDict(from_attributes=True)



