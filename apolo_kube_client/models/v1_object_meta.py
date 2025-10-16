from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from .v1_managed_fields_entry import V1ManagedFieldsEntry
from .v1_owner_reference import V1OwnerReference

__all__ = ("V1ObjectMeta",)


class V1ObjectMeta(BaseModel):
    annotations: dict[str, str] | None = Field(None, alias="annotations")

    creation_timestamp: datetime | None = Field(None, alias="creationTimestamp")

    deletion_grace_period_seconds: int | None = Field(
        None, alias="deletionGracePeriodSeconds"
    )

    deletion_timestamp: datetime | None = Field(None, alias="deletionTimestamp")

    finalizers: list[str] | None = Field(None, alias="finalizers")

    generate_name: str | None = Field(None, alias="generateName")

    generation: int | None = Field(None, alias="generation")

    labels: dict[str, str] | None = Field(None, alias="labels")

    managed_fields: list[V1ManagedFieldsEntry] | None = Field(
        None, alias="managedFields"
    )

    name: str | None = Field(None, alias="name")

    namespace: str | None = Field(None, alias="namespace")

    owner_references: list[V1OwnerReference] | None = Field(
        None, alias="ownerReferences"
    )

    resource_version: str | None = Field(None, alias="resourceVersion")

    self_link: str | None = Field(None, alias="selfLink")

    uid: str | None = Field(None, alias="uid")
