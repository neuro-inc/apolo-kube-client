from pydantic import AliasChoices, Field
from .base import ResourceModel
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1beta1VolumeAttributesClass",)


class V1beta1VolumeAttributesClass(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    driver_name: str | None = Field(
        default=None,
        serialization_alias="driverName",
        validation_alias=AliasChoices("driver_name", "driverName"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    parameters: dict[str, str] = {}
