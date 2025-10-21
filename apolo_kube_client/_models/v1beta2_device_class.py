from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1beta2_device_class_spec import V1beta2DeviceClassSpec
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta2DeviceClass",)


class V1beta2DeviceClass(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[
        V1beta2DeviceClassSpec,
        BeforeValidator(_default_if_none(V1beta2DeviceClassSpec)),
    ] = Field(default_factory=lambda: V1beta2DeviceClassSpec())
