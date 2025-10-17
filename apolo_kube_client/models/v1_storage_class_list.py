from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_storage_class import V1StorageClass

__all__ = ("V1StorageClassList",)


class V1StorageClassList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1StorageClass] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
