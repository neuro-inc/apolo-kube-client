from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_managed_fields_entry import V1ManagedFieldsEntry
from .v1_owner_reference import V1OwnerReference
from datetime import datetime

__all__ = ("V1ObjectMeta",)


class V1ObjectMeta(BaseModel):
    annotations: dict[str, str] = Field(default_factory=lambda: {})

    creation_timestamp: datetime | None = Field(
        default_factory=lambda: None, alias="creationTimestamp"
    )

    deletion_grace_period_seconds: int | None = Field(
        default_factory=lambda: None, alias="deletionGracePeriodSeconds"
    )

    deletion_timestamp: datetime | None = Field(
        default_factory=lambda: None, alias="deletionTimestamp"
    )

    finalizers: list[str] = Field(default_factory=lambda: [])

    generate_name: str | None = Field(
        default_factory=lambda: None, alias="generateName"
    )

    generation: int | None = Field(default_factory=lambda: None)

    labels: dict[str, str] = Field(default_factory=lambda: {})

    managed_fields: list[V1ManagedFieldsEntry] = Field(
        default_factory=lambda: [], alias="managedFields"
    )

    name: str | None = Field(default_factory=lambda: None)

    namespace: str | None = Field(default_factory=lambda: None)

    owner_references: list[V1OwnerReference] = Field(
        default_factory=lambda: [], alias="ownerReferences"
    )

    resource_version: str | None = Field(
        default_factory=lambda: None, alias="resourceVersion"
    )

    self_link: str | None = Field(default_factory=lambda: None, alias="selfLink")

    uid: str | None = Field(default_factory=lambda: None)
