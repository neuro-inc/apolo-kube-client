from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_device_class_spec import V1DeviceClassSpec
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1DeviceClass",)


class V1DeviceClass(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1DeviceClassSpec = Field(
        default_factory=lambda: V1DeviceClassSpec(), alias="spec"
    )
