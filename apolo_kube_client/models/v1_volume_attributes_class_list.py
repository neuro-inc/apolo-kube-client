from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_volume_attributes_class import V1VolumeAttributesClass

__all__ = ("V1VolumeAttributesClassList",)


class V1VolumeAttributesClassList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1VolumeAttributesClass] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
