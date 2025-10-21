from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1alpha1_storage_version_migration_spec import V1alpha1StorageVersionMigrationSpec
from .v1alpha1_storage_version_migration_status import (
    V1alpha1StorageVersionMigrationStatus,
)
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1alpha1StorageVersionMigration",)


class V1alpha1StorageVersionMigration(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[
        V1alpha1StorageVersionMigrationSpec,
        BeforeValidator(_default_if_none(V1alpha1StorageVersionMigrationSpec)),
    ] = Field(default_factory=lambda: V1alpha1StorageVersionMigrationSpec())

    status: Annotated[
        V1alpha1StorageVersionMigrationStatus,
        BeforeValidator(_default_if_none(V1alpha1StorageVersionMigrationStatus)),
    ] = Field(default_factory=lambda: V1alpha1StorageVersionMigrationStatus())
