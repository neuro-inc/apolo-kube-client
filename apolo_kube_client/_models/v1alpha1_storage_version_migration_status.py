from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1alpha1_migration_condition import V1alpha1MigrationCondition
from pydantic import BeforeValidator

__all__ = ("V1alpha1StorageVersionMigrationStatus",)


class V1alpha1StorageVersionMigrationStatus(BaseModel):
    """Status of the storage version migration."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.storagemigration.v1alpha1.StorageVersionMigrationStatus"
    )

    conditions: Annotated[
        list[V1alpha1MigrationCondition],
        Field(
            description="""The latest available observations of the migration's current state.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    resource_version: Annotated[
        str | None,
        Field(
            alias="resourceVersion",
            description="""ResourceVersion to compare with the GC cache for performing the migration. This is the current resource version of given group, version and resource when kube-controller-manager first observes this StorageVersionMigration resource.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
