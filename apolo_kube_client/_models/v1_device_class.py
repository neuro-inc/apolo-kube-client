from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .v1_device_class_spec import V1DeviceClassSpec
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DeviceClass",)


class V1DeviceClass(ResourceModel):
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
        V1DeviceClassSpec, BeforeValidator(_default_if_none(V1DeviceClassSpec))
    ] = Field(default_factory=lambda: V1DeviceClassSpec())
