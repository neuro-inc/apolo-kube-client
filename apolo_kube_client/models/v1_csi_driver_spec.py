from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .storage_v1_token_request import StorageV1TokenRequest

__all__ = ("V1CSIDriverSpec",)


class V1CSIDriverSpec(BaseModel):
    attach_required: bool | None = Field(
        default=None,
        serialization_alias="attachRequired",
        validation_alias=AliasChoices("attach_required", "attachRequired"),
    )

    fs_group_policy: str | None = Field(
        default=None,
        serialization_alias="fsGroupPolicy",
        validation_alias=AliasChoices("fs_group_policy", "fsGroupPolicy"),
    )

    node_allocatable_update_period_seconds: int | None = Field(
        default=None,
        serialization_alias="nodeAllocatableUpdatePeriodSeconds",
        validation_alias=AliasChoices(
            "node_allocatable_update_period_seconds",
            "nodeAllocatableUpdatePeriodSeconds",
        ),
    )

    pod_info_on_mount: bool | None = Field(
        default=None,
        serialization_alias="podInfoOnMount",
        validation_alias=AliasChoices("pod_info_on_mount", "podInfoOnMount"),
    )

    requires_republish: bool | None = Field(
        default=None,
        serialization_alias="requiresRepublish",
        validation_alias=AliasChoices("requires_republish", "requiresRepublish"),
    )

    se_linux_mount: bool | None = Field(
        default=None,
        serialization_alias="seLinuxMount",
        validation_alias=AliasChoices("se_linux_mount", "seLinuxMount"),
    )

    storage_capacity: bool | None = Field(
        default=None,
        serialization_alias="storageCapacity",
        validation_alias=AliasChoices("storage_capacity", "storageCapacity"),
    )

    token_requests: list[StorageV1TokenRequest] = Field(
        default=[],
        serialization_alias="tokenRequests",
        validation_alias=AliasChoices("token_requests", "tokenRequests"),
    )

    volume_lifecycle_modes: list[str] = Field(
        default=[],
        serialization_alias="volumeLifecycleModes",
        validation_alias=AliasChoices("volume_lifecycle_modes", "volumeLifecycleModes"),
    )
