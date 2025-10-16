from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_modify_volume_status import V1ModifyVolumeStatus
from .v1_persistent_volume_claim_condition import V1PersistentVolumeClaimCondition

__all__ = ("V1PersistentVolumeClaimStatus",)


class V1PersistentVolumeClaimStatus(BaseModel):
    access_modes: list[str] | None = Field(None, alias="accessModes")

    allocated_resource_statuses: dict[str, str] | None = Field(
        None, alias="allocatedResourceStatuses"
    )

    allocated_resources: dict[str, str] | None = Field(None, alias="allocatedResources")

    capacity: dict[str, str] | None = Field(None, alias="capacity")

    conditions: list[V1PersistentVolumeClaimCondition] | None = Field(
        None, alias="conditions"
    )

    current_volume_attributes_class_name: str | None = Field(
        None, alias="currentVolumeAttributesClassName"
    )

    modify_volume_status: V1ModifyVolumeStatus | None = Field(
        None, alias="modifyVolumeStatus"
    )

    phase: str | None = Field(None, alias="phase")
