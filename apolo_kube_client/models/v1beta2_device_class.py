from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1beta2_device_class_spec import V1beta2DeviceClassSpec

__all__ = ("V1beta2DeviceClass",)


class V1beta2DeviceClass(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1beta2DeviceClassSpec = Field(
        default_factory=lambda: V1beta2DeviceClassSpec()
    )
