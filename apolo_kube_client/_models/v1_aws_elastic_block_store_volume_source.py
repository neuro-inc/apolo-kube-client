from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1AWSElasticBlockStoreVolumeSource",)


class V1AWSElasticBlockStoreVolumeSource(BaseModel):
    """Represents a Persistent Disk resource in AWS.

    An AWS EBS disk must exist before mounting to a container. The disk must also be in the same AWS zone as the kubelet. An AWS EBS disk can only be mounted as read/write once. AWS EBS volumes support ownership management and SELinux relabeling."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.AWSElasticBlockStoreVolumeSource"
    )

    fs_type: Annotated[
        str | None,
        Field(
            alias="fsType",
            description="""fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    partition: Annotated[
        int | None,
        Field(
            description="""partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    read_only: Annotated[
        bool | None,
        Field(
            alias="readOnly",
            description="""readOnly value true will force the readOnly setting in VolumeMounts. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    volume_id: Annotated[
        str,
        Field(
            alias="volumeID",
            description="""volumeID is unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore""",
        ),
    ]
