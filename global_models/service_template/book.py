from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, constr


class BookBase(BaseModel):
    id: Optional[int] = None
    name: Optional[constr(max_length=63)] = None
    author: Optional[constr(max_length=63)] = None
    price: Optional[Decimal] = None


class BookCreate(BookBase):
    name: constr(max_length=63)
    author: constr(max_length=63)
    price: Decimal


class BookUpdatePrice(BookBase):
    id: int
    price: Decimal


class BookInDb(BookBase):
    id: int
    creation_date: Optional[datetime]

    class Config:
        orm_mode = True
