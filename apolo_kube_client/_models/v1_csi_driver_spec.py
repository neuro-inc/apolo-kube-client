from pydantic import AliasChoices, BaseModel, Field
from .storage_v1_token_request import StorageV1TokenRequest
from .utils import _collection_if_none
from .utils import _exclude_if
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CSIDriverSpec",)


class V1CSIDriverSpec(BaseModel):
    attach_required: bool | None = Field(
        default=None,
        serialization_alias="attachRequired",
        validation_alias=AliasChoices("attach_required", "attachRequired"),
        exclude_if=_exclude_if,
    )

    fs_group_policy: str | None = Field(
        default=None,
        serialization_alias="fsGroupPolicy",
        validation_alias=AliasChoices("fs_group_policy", "fsGroupPolicy"),
        exclude_if=_exclude_if,
    )

    node_allocatable_update_period_seconds: int | None = Field(
        default=None,
        serialization_alias="nodeAllocatableUpdatePeriodSeconds",
        validation_alias=AliasChoices(
            "node_allocatable_update_period_seconds",
            "nodeAllocatableUpdatePeriodSeconds",
        ),
        exclude_if=_exclude_if,
    )

    pod_info_on_mount: bool | None = Field(
        default=None,
        serialization_alias="podInfoOnMount",
        validation_alias=AliasChoices("pod_info_on_mount", "podInfoOnMount"),
        exclude_if=_exclude_if,
    )

    requires_republish: bool | None = Field(
        default=None,
        serialization_alias="requiresRepublish",
        validation_alias=AliasChoices("requires_republish", "requiresRepublish"),
        exclude_if=_exclude_if,
    )

    se_linux_mount: bool | None = Field(
        default=None,
        serialization_alias="seLinuxMount",
        validation_alias=AliasChoices("se_linux_mount", "seLinuxMount"),
        exclude_if=_exclude_if,
    )

    storage_capacity: bool | None = Field(
        default=None,
        serialization_alias="storageCapacity",
        validation_alias=AliasChoices("storage_capacity", "storageCapacity"),
        exclude_if=_exclude_if,
    )

    token_requests: Annotated[
        list[StorageV1TokenRequest], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="tokenRequests",
        validation_alias=AliasChoices("token_requests", "tokenRequests"),
        exclude_if=_exclude_if,
    )

    volume_lifecycle_modes: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="volumeLifecycleModes",
        validation_alias=AliasChoices("volume_lifecycle_modes", "volumeLifecycleModes"),
        exclude_if=_exclude_if,
    )
