from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1alpha1_storage_version import V1alpha1StorageVersion

__all__ = ("V1alpha1StorageVersionList",)


class V1alpha1StorageVersionList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1alpha1StorageVersion] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
