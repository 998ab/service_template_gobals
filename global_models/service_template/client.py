from typing import List

from pydantic import BaseModel, constr

from global_models.service_template.client_role import ClientRole


class Client(BaseModel):
    id: int
    name: constr(max_length=63)
    roles: List[ClientRole]

    class Config:
        orm_mode = True
