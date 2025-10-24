from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1VsphereVirtualDiskVolumeSource",)


class V1VsphereVirtualDiskVolumeSource(BaseModel):
    """Represents a vSphere volume resource."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.VsphereVirtualDiskVolumeSource"
    )

    fs_type: Annotated[
        str | None,
        Field(
            alias="fsType",
            description="""fsType is filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    storage_policy_id: Annotated[
        str | None,
        Field(
            alias="storagePolicyID",
            description="""storagePolicyID is the storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    storage_policy_name: Annotated[
        str | None,
        Field(
            alias="storagePolicyName",
            description="""storagePolicyName is the storage Policy Based Management (SPBM) profile name.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    volume_path: Annotated[
        str,
        Field(
            alias="volumePath",
            description="""volumePath is the path that identifies vSphere volume vmdk""",
        ),
    ]
