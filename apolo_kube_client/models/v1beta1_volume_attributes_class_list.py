from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1beta1_volume_attributes_class import V1beta1VolumeAttributesClass

__all__ = ("V1beta1VolumeAttributesClassList",)


class V1beta1VolumeAttributesClassList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1beta1VolumeAttributesClass] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
