from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1LocalVolumeSource",)


class V1LocalVolumeSource(BaseModel):
    """Local represents directly-attached storage with node affinity"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.LocalVolumeSource"

    fs_type: Annotated[
        str | None,
        Field(
            alias="fsType",
            description="""fsType is the filesystem type to mount. It applies only when the Path is a block device. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default value is to auto-select a filesystem if unspecified.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    path: Annotated[
        str,
        Field(
            description="""path of the full path to the volume on the node. It can be either a directory or block device (disk, partition, ...)."""
        ),
    ]
