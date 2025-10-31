from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1alpha1_storage_version_migration_spec import V1alpha1StorageVersionMigrationSpec
from .v1alpha1_storage_version_migration_status import (
    V1alpha1StorageVersionMigrationStatus,
)
from pydantic import BeforeValidator

__all__ = ("V1alpha1StorageVersionMigration",)


class V1alpha1StorageVersionMigration(ResourceModel):
    """StorageVersionMigration represents a migration of stored data to the latest storage version."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.storagemigration.v1alpha1.StorageVersionMigration"
    )

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="storagemigration.k8s.io",
        kind="StorageVersionMigration",
        version="v1alpha1",
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "storagemigration.k8s.io/v1alpha1"

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "StorageVersionMigration"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    spec: Annotated[
        V1alpha1StorageVersionMigrationSpec | None,
        Field(
            description="""Specification of the migration.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    status: Annotated[
        V1alpha1StorageVersionMigrationStatus,
        Field(
            description="""Status of the migration.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1alpha1StorageVersionMigrationStatus)),
    ] = V1alpha1StorageVersionMigrationStatus()
