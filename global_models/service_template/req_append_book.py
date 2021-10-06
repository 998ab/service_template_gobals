from typing import Optional
from pydantic import BaseModel, constr


class ReqAppendBook(BaseModel):
    client_id: Optional[int]
    book_id: constr(max_length=63)
