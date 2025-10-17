from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1beta1_device_class import V1beta1DeviceClass

__all__ = ("V1beta1DeviceClassList",)


class V1beta1DeviceClassList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1beta1DeviceClass] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
