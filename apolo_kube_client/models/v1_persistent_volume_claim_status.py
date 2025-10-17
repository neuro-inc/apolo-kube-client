from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_modify_volume_status import V1ModifyVolumeStatus
from .v1_persistent_volume_claim_condition import V1PersistentVolumeClaimCondition

__all__ = ("V1PersistentVolumeClaimStatus",)


class V1PersistentVolumeClaimStatus(BaseModel):
    access_modes: list[str] = Field(default_factory=lambda: [], alias="accessModes")

    allocated_resource_statuses: dict[str, str] = Field(
        default_factory=lambda: {}, alias="allocatedResourceStatuses"
    )

    allocated_resources: dict[str, str] = Field(
        default_factory=lambda: {}, alias="allocatedResources"
    )

    capacity: dict[str, str] = Field(default_factory=lambda: {})

    conditions: list[V1PersistentVolumeClaimCondition] = Field(
        default_factory=lambda: []
    )

    current_volume_attributes_class_name: str | None = Field(
        default_factory=lambda: None, alias="currentVolumeAttributesClassName"
    )

    modify_volume_status: V1ModifyVolumeStatus = Field(
        default_factory=lambda: V1ModifyVolumeStatus(), alias="modifyVolumeStatus"
    )

    phase: str | None = Field(default_factory=lambda: None)
