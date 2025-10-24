from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1GCEPersistentDiskVolumeSource",)


class V1GCEPersistentDiskVolumeSource(BaseModel):
    """Represents a Persistent Disk resource in Google Compute Engine.

    A GCE PD must exist before mounting to a container. The disk must also be in the same GCE project and zone as the kubelet. A GCE PD can only be mounted as read/write once or read-only many times. GCE PDs support ownership management and SELinux relabeling."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.GCEPersistentDiskVolumeSource"
    )

    fs_type: Annotated[
        str | None,
        Field(
            alias="fsType",
            description="""fsType is filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    partition: Annotated[
        int | None,
        Field(
            description="""partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    pd_name: Annotated[
        str,
        Field(
            alias="pdName",
            description="""pdName is unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk""",
        ),
    ]

    read_only: Annotated[
        bool | None,
        Field(
            alias="readOnly",
            description="""readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
