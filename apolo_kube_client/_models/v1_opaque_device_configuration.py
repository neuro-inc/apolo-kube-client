from pydantic import BaseModel
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1OpaqueDeviceConfiguration",)


class V1OpaqueDeviceConfiguration(BaseModel):
    driver: str | None = None

    parameters: JsonType = {}
