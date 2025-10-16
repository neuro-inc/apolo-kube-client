from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1alpha1_storage_version_migration import V1alpha1StorageVersionMigration

__all__ = ("V1alpha1StorageVersionMigrationList",)


class V1alpha1StorageVersionMigrationList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1alpha1StorageVersionMigration] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
