from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1AzureDiskVolumeSource",)


class V1AzureDiskVolumeSource(BaseModel):
    """AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.AzureDiskVolumeSource"

    caching_mode: Annotated[
        str | None,
        Field(
            alias="cachingMode",
            description="""cachingMode is the Host Caching mode: None, Read Only, Read Write.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    disk_name: Annotated[
        str,
        Field(
            alias="diskName",
            description="""diskName is the Name of the data disk in the blob storage""",
        ),
    ]

    disk_uri: Annotated[
        str,
        Field(
            alias="diskURI",
            description="""diskURI is the URI of data disk in the blob storage""",
        ),
    ]

    fs_type: Annotated[
        str | None,
        Field(
            alias="fsType",
            description="""fsType is Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    kind: Annotated[
        str | None,
        Field(
            description="""kind expected values are Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    read_only: Annotated[
        bool | None,
        Field(
            alias="readOnly",
            description="""readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
