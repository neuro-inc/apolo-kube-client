from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1alpha1_storage_version_migration_spec import V1alpha1StorageVersionMigrationSpec
from .v1alpha1_storage_version_migration_status import (
    V1alpha1StorageVersionMigrationStatus,
)


class V1alpha1StorageVersionMigration(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1alpha1StorageVersionMigrationSpec | None = Field(None, alias="spec")

    status: V1alpha1StorageVersionMigrationStatus | None = Field(None, alias="status")
