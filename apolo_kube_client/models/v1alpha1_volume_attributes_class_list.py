from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1alpha1_volume_attributes_class import V1alpha1VolumeAttributesClass

__all__ = ("V1alpha1VolumeAttributesClassList",)


class V1alpha1VolumeAttributesClassList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1alpha1VolumeAttributesClass] = Field(default_factory=lambda: [])

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
