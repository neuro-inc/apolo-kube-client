from pydantic import BaseModel, Field

from .storage_v1_token_request import StorageV1TokenRequest


class V1CSIDriverSpec(BaseModel):
    attach_required: bool | None = Field(None, alias="attachRequired")

    fs_group_policy: str | None = Field(None, alias="fsGroupPolicy")

    pod_info_on_mount: bool | None = Field(None, alias="podInfoOnMount")

    requires_republish: bool | None = Field(None, alias="requiresRepublish")

    se_linux_mount: bool | None = Field(None, alias="seLinuxMount")

    storage_capacity: bool | None = Field(None, alias="storageCapacity")

    token_requests: list[StorageV1TokenRequest] | None = Field(
        None, alias="tokenRequests"
    )

    volume_lifecycle_modes: list[str] | None = Field(None, alias="volumeLifecycleModes")
