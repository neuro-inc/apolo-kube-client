from __future__ import annotations

from pydantic import BaseModel, Field

from apolo_kube_client._typedefs import JsonType

__all__ = ("V1alpha3OpaqueDeviceConfiguration",)


class V1alpha3OpaqueDeviceConfiguration(BaseModel):
    driver: str | None = Field(None, alias="driver")

    parameters: JsonType | None = Field(None, alias="parameters")
