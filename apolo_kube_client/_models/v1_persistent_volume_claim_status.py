from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_modify_volume_status import V1ModifyVolumeStatus
from .v1_persistent_volume_claim_condition import V1PersistentVolumeClaimCondition
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PersistentVolumeClaimStatus",)


class V1PersistentVolumeClaimStatus(BaseModel):
    access_modes: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="accessModes",
            validation_alias=AliasChoices("access_modes", "accessModes"),
        )
    )

    allocated_resource_statuses: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = Field(
        default={},
        serialization_alias="allocatedResourceStatuses",
        validation_alias=AliasChoices(
            "allocated_resource_statuses", "allocatedResourceStatuses"
        ),
    )

    allocated_resources: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = Field(
        default={},
        serialization_alias="allocatedResources",
        validation_alias=AliasChoices("allocated_resources", "allocatedResources"),
    )

    capacity: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = {}

    conditions: Annotated[
        list[V1PersistentVolumeClaimCondition],
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    current_volume_attributes_class_name: str | None = Field(
        default=None,
        serialization_alias="currentVolumeAttributesClassName",
        validation_alias=AliasChoices(
            "current_volume_attributes_class_name", "currentVolumeAttributesClassName"
        ),
    )

    modify_volume_status: Annotated[
        V1ModifyVolumeStatus, BeforeValidator(_default_if_none(V1ModifyVolumeStatus))
    ] = Field(
        default_factory=lambda: V1ModifyVolumeStatus(),
        serialization_alias="modifyVolumeStatus",
        validation_alias=AliasChoices("modify_volume_status", "modifyVolumeStatus"),
    )

    phase: str | None = None
