from pydantic import BaseModel
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1TCPSocketAction",)


class V1TCPSocketAction(BaseModel):
    host: str | None = None

    port: JsonType = {}
