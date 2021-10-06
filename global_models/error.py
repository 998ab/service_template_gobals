from typing import Optional
from pydantic.main import BaseModel


class Error(BaseModel):
    message: Optional[str]
    code: Optional[str]


__all__ = [
    "Error",
]
