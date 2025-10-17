from __future__ import annotations
from pydantic import BaseModel, Field
from .v1alpha1_migration_condition import V1alpha1MigrationCondition

__all__ = ("V1alpha1StorageVersionMigrationStatus",)


class V1alpha1StorageVersionMigrationStatus(BaseModel):
    conditions: list[V1alpha1MigrationCondition] = Field(default_factory=lambda: [])

    resource_version: str | None = Field(
        default_factory=lambda: None, alias="resourceVersion"
    )
