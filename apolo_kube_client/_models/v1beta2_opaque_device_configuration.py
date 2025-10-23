from pydantic import BaseModel, Field
from .utils import _exclude_if
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1beta2OpaqueDeviceConfiguration",)


class V1beta2OpaqueDeviceConfiguration(BaseModel):
    driver: str | None = Field(default=None, exclude_if=_exclude_if)

    parameters: JsonType = Field(default={}, exclude_if=_exclude_if)
