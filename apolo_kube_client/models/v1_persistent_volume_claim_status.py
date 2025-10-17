from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_modify_volume_status import V1ModifyVolumeStatus
from .v1_persistent_volume_claim_condition import V1PersistentVolumeClaimCondition

__all__ = ("V1PersistentVolumeClaimStatus",)


class V1PersistentVolumeClaimStatus(BaseModel):
    access_modes: list[str] = Field(
        default=[],
        serialization_alias="accessModes",
        validation_alias=AliasChoices("access_modes", "accessModes"),
    )

    allocated_resource_statuses: dict[str, str] = Field(
        default={},
        serialization_alias="allocatedResourceStatuses",
        validation_alias=AliasChoices(
            "allocated_resource_statuses", "allocatedResourceStatuses"
        ),
    )

    allocated_resources: dict[str, str] = Field(
        default={},
        serialization_alias="allocatedResources",
        validation_alias=AliasChoices("allocated_resources", "allocatedResources"),
    )

    capacity: dict[str, str] = Field(default={})

    conditions: list[V1PersistentVolumeClaimCondition] = Field(default=[])

    current_volume_attributes_class_name: str | None = Field(
        default=None,
        serialization_alias="currentVolumeAttributesClassName",
        validation_alias=AliasChoices(
            "current_volume_attributes_class_name", "currentVolumeAttributesClassName"
        ),
    )

    modify_volume_status: V1ModifyVolumeStatus = Field(
        default_factory=lambda: V1ModifyVolumeStatus(),
        serialization_alias="modifyVolumeStatus",
        validation_alias=AliasChoices("modify_volume_status", "modifyVolumeStatus"),
    )

    phase: str | None = Field(default=None)
