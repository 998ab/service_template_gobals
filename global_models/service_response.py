from typing import Any, Optional

from pydantic.main import BaseModel

from global_models.status import Status


class ServiceResponse(BaseModel):
    tracking_id: Optional[str]
    status: Optional[Status]
    payload: Optional[Any]
    status_code: int = 500
    content_type: str = "application/json"

    def is_successful(self):
        return self.status is Status.OK

    def to_json(self):
        return self.json(exclude={"status_code", "content_type"})


__all__ = [
    'ServiceResponse',
]
