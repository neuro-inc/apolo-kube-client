from __future__ import annotations
from pydantic import BaseModel, Field
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1beta1OpaqueDeviceConfiguration",)


class V1beta1OpaqueDeviceConfiguration(BaseModel):
    driver: str | None = Field(default_factory=lambda: None)

    parameters: JsonType = Field(default_factory=lambda: {})
