from __future__ import annotations
from pydantic import BaseModel, Field
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1WatchEvent",)


class V1WatchEvent(BaseModel):
    object: JsonType = Field(default={})

    type: str | None = Field(default=None)
