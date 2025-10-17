from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1alpha1_storage_version_migration_spec import V1alpha1StorageVersionMigrationSpec
from .v1alpha1_storage_version_migration_status import (
    V1alpha1StorageVersionMigrationStatus,
)

__all__ = ("V1alpha1StorageVersionMigration",)


class V1alpha1StorageVersionMigration(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    spec: V1alpha1StorageVersionMigrationSpec = Field(
        default_factory=lambda: V1alpha1StorageVersionMigrationSpec()
    )

    status: V1alpha1StorageVersionMigrationStatus = Field(
        default_factory=lambda: V1alpha1StorageVersionMigrationStatus()
    )
