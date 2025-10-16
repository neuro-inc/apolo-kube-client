from __future__ import annotations
from pydantic import BaseModel, Field
from .storage_v1_token_request import StorageV1TokenRequest

__all__ = ("V1CSIDriverSpec",)


class V1CSIDriverSpec(BaseModel):
    attach_required: bool | None = Field(
        default_factory=lambda: None, alias="attachRequired"
    )

    fs_group_policy: str | None = Field(
        default_factory=lambda: None, alias="fsGroupPolicy"
    )

    node_allocatable_update_period_seconds: int | None = Field(
        default_factory=lambda: None, alias="nodeAllocatableUpdatePeriodSeconds"
    )

    pod_info_on_mount: bool | None = Field(
        default_factory=lambda: None, alias="podInfoOnMount"
    )

    requires_republish: bool | None = Field(
        default_factory=lambda: None, alias="requiresRepublish"
    )

    se_linux_mount: bool | None = Field(
        default_factory=lambda: None, alias="seLinuxMount"
    )

    storage_capacity: bool | None = Field(
        default_factory=lambda: None, alias="storageCapacity"
    )

    token_requests: list[StorageV1TokenRequest] = Field(
        default_factory=lambda: [], alias="tokenRequests"
    )

    volume_lifecycle_modes: list[str] = Field(
        default_factory=lambda: [], alias="volumeLifecycleModes"
    )
