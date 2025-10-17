from pydantic import BaseModel
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1beta2OpaqueDeviceConfiguration",)


class V1beta2OpaqueDeviceConfiguration(BaseModel):
    driver: str | None = None

    parameters: JsonType = {}
