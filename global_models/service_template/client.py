from datetime import datetime
from typing import Optional

from pydantic import BaseModel, constr

from global_models.service_template.client_role import ClientRole


class Client(BaseModel):
    id: Optional[int]
    name: constr(max_length=63)
    role: ClientRole
    creation_date: Optional[datetime]

    class Config:
        orm_mode = True
