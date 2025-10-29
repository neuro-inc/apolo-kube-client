from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_secret_reference import V1SecretReference
from pydantic import BeforeValidator

__all__ = ("V1RBDPersistentVolumeSource",)


class V1RBDPersistentVolumeSource(BaseModel):
    """Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.RBDPersistentVolumeSource"
    )

    fs_type: Annotated[
        str | None,
        Field(
            alias="fsType",
            description="""fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    image: Annotated[
        str,
        Field(
            description="""image is the rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it"""
        ),
    ]

    keyring: Annotated[
        str | None,
        Field(
            description="""keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    monitors: Annotated[
        list[str],
        Field(
            description="""monitors is a collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it"""
        ),
    ]

    pool: Annotated[
        str | None,
        Field(
            description="""pool is the rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    read_only: Annotated[
        bool | None,
        Field(
            alias="readOnly",
            description="""readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    secret_ref: Annotated[
        V1SecretReference,
        Field(
            alias="secretRef",
            description="""secretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1SecretReference)),
    ] = V1SecretReference()

    user: Annotated[
        str | None,
        Field(
            description="""user is the rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
