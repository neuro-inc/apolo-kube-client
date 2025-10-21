from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1alpha1_migration_condition import V1alpha1MigrationCondition
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1alpha1StorageVersionMigrationStatus",)


class V1alpha1StorageVersionMigrationStatus(BaseModel):
    conditions: Annotated[
        list[V1alpha1MigrationCondition], BeforeValidator(_collection_if_none("[]"))
    ] = []

    resource_version: str | None = Field(
        default=None,
        serialization_alias="resourceVersion",
        validation_alias=AliasChoices("resource_version", "resourceVersion"),
    )
