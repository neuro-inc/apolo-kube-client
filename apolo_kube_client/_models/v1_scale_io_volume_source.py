from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_local_object_reference import V1LocalObjectReference

__all__ = ("V1ScaleIOVolumeSource",)


class V1ScaleIOVolumeSource(BaseModel):
    """ScaleIOVolumeSource represents a persistent ScaleIO volume"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ScaleIOVolumeSource"

    fs_type: Annotated[
        str | None,
        Field(
            alias="fsType",
            description="""fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs".""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    gateway: Annotated[
        str,
        Field(
            description="""gateway is the host address of the ScaleIO API Gateway."""
        ),
    ]

    protection_domain: Annotated[
        str | None,
        Field(
            alias="protectionDomain",
            description="""protectionDomain is the name of the ScaleIO Protection Domain for the configured storage.""",
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

    secret_ref: Annotated[
        V1LocalObjectReference,
        Field(
            alias="secretRef",
            description="""secretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.""",
        ),
    ]

    ssl_enabled: Annotated[
        bool | None,
        Field(
            alias="sslEnabled",
            description="""sslEnabled Flag enable/disable SSL communication with Gateway, default false""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    storage_mode: Annotated[
        str | None,
        Field(
            alias="storageMode",
            description="""storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    storage_pool: Annotated[
        str | None,
        Field(
            alias="storagePool",
            description="""storagePool is the ScaleIO Storage Pool associated with the protection domain.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    system: Annotated[
        str,
        Field(
            description="""system is the name of the storage system as configured in ScaleIO."""
        ),
    ]

    volume_name: Annotated[
        str | None,
        Field(
            alias="volumeName",
            description="""volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
