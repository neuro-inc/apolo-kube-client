from pydantic import BaseModel, Field
from .utils import _exclude_if
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1TCPSocketAction",)


class V1TCPSocketAction(BaseModel):
    host: str | None = Field(default=None, exclude_if=_exclude_if)

    port: JsonType = Field(default={}, exclude_if=_exclude_if)
