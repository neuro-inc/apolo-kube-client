from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_resource_slice import V1ResourceSlice

__all__ = ("V1ResourceSliceList",)


class V1ResourceSliceList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1ResourceSlice] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
