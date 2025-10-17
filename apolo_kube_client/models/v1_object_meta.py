from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_managed_fields_entry import V1ManagedFieldsEntry
from .v1_owner_reference import V1OwnerReference
from datetime import datetime

__all__ = ("V1ObjectMeta",)


class V1ObjectMeta(BaseModel):
    annotations: dict[str, str] = Field(default={})

    creation_timestamp: datetime | None = Field(
        default=None,
        serialization_alias="creationTimestamp",
        validation_alias=AliasChoices("creation_timestamp", "creationTimestamp"),
    )

    deletion_grace_period_seconds: int | None = Field(
        default=None,
        serialization_alias="deletionGracePeriodSeconds",
        validation_alias=AliasChoices(
            "deletion_grace_period_seconds", "deletionGracePeriodSeconds"
        ),
    )

    deletion_timestamp: datetime | None = Field(
        default=None,
        serialization_alias="deletionTimestamp",
        validation_alias=AliasChoices("deletion_timestamp", "deletionTimestamp"),
    )

    finalizers: list[str] = Field(default=[])

    generate_name: str | None = Field(
        default=None,
        serialization_alias="generateName",
        validation_alias=AliasChoices("generate_name", "generateName"),
    )

    generation: int | None = Field(default=None)

    labels: dict[str, str] = Field(default={})

    managed_fields: list[V1ManagedFieldsEntry] = Field(
        default=[],
        serialization_alias="managedFields",
        validation_alias=AliasChoices("managed_fields", "managedFields"),
    )

    name: str

    namespace: str | None = Field(default=None)

    owner_references: list[V1OwnerReference] = Field(
        default=[],
        serialization_alias="ownerReferences",
        validation_alias=AliasChoices("owner_references", "ownerReferences"),
    )

    resource_version: str | None = Field(
        default=None,
        serialization_alias="resourceVersion",
        validation_alias=AliasChoices("resource_version", "resourceVersion"),
    )

    self_link: str | None = Field(
        default=None,
        serialization_alias="selfLink",
        validation_alias=AliasChoices("self_link", "selfLink"),
    )

    uid: str | None = Field(default=None)
