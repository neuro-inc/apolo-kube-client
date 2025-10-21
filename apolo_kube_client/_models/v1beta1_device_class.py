from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1beta1_device_class_spec import V1beta1DeviceClassSpec
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1DeviceClass",)


class V1beta1DeviceClass(ResourceModel):
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
        V1beta1DeviceClassSpec,
        BeforeValidator(_default_if_none(V1beta1DeviceClassSpec)),
    ] = Field(default_factory=lambda: V1beta1DeviceClassSpec())
