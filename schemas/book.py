from pydentic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    published_year: Optional[int] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookRead(BookBase):
    id: int

    class Config:
        orm_mode = True



