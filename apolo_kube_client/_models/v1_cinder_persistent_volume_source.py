from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_secret_reference import V1SecretReference
from pydantic import BeforeValidator

__all__ = ("V1CinderPersistentVolumeSource",)


class V1CinderPersistentVolumeSource(BaseModel):
    """Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.CinderPersistentVolumeSource"
    )

    fs_type: Annotated[
        str | None,
        Field(
            alias="fsType",
            description="""fsType Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    read_only: Annotated[
        bool | None,
        Field(
            alias="readOnly",
            description="""readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    secret_ref: Annotated[
        V1SecretReference,
        Field(
            alias="secretRef",
            description="""secretRef is Optional: points to a secret object containing parameters used to connect to OpenStack.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1SecretReference)),
    ] = V1SecretReference()

    volume_id: Annotated[
        str,
        Field(
            alias="volumeID",
            description="""volumeID used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md""",
        ),
    ]
