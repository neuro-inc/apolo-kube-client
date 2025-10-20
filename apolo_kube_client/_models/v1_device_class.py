from pydantic import AliasChoices, Field
from .base import ResourceModel
from .v1_device_class_spec import V1DeviceClassSpec
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1DeviceClass",)


class V1DeviceClass(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1DeviceClassSpec = Field(default_factory=lambda: V1DeviceClassSpec())
