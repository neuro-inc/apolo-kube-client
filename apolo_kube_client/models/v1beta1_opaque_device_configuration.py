from pydantic import BaseModel
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1beta1OpaqueDeviceConfiguration",)


class V1beta1OpaqueDeviceConfiguration(BaseModel):
    driver: str | None = None

    parameters: JsonType = {}
