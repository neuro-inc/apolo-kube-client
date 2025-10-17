from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1beta2_device_class import V1beta2DeviceClass

__all__ = ("V1beta2DeviceClassList",)


class V1beta2DeviceClassList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1beta2DeviceClass] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
