from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1alpha1_group_version_resource import V1alpha1GroupVersionResource

__all__ = ("V1alpha1StorageVersionMigrationSpec",)


class V1alpha1StorageVersionMigrationSpec(BaseModel):
    """Spec of the storage version migration."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.storagemigration.v1alpha1.StorageVersionMigrationSpec"
    )

    continue_token: Annotated[
        str | None,
        Field(
            alias="continueToken",
            description="""The token used in the list options to get the next chunk of objects to migrate. When the .status.conditions indicates the migration is "Running", users can use this token to check the progress of the migration.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    resource: Annotated[
        V1alpha1GroupVersionResource,
        Field(
            description="""The resource that is being migrated. The migrator sends requests to the endpoint serving the resource. Immutable."""
        ),
    ]
