from __future__ import annotations
from pydantic import BaseModel, Field
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1beta2OpaqueDeviceConfiguration",)


class V1beta2OpaqueDeviceConfiguration(BaseModel):
    driver: str | None = Field(default=None)

    parameters: JsonType = Field(default={})
