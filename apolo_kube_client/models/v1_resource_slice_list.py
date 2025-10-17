from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_resource_slice import V1ResourceSlice

__all__ = ("V1ResourceSliceList",)


class V1ResourceSliceList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1ResourceSlice] = Field(default_factory=lambda: [])

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
