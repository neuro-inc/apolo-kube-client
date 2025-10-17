from pydantic import BaseModel
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1WatchEvent",)


class V1WatchEvent(BaseModel):
    object: JsonType = {}

    type: str | None = None
