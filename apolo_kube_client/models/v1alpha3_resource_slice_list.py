from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1alpha3_resource_slice import V1alpha3ResourceSlice

__all__ = ("V1alpha3ResourceSliceList",)


class V1alpha3ResourceSliceList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1alpha3ResourceSlice] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
