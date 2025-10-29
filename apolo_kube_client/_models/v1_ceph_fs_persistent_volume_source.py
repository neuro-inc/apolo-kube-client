from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_secret_reference import V1SecretReference
from pydantic import BeforeValidator

__all__ = ("V1CephFSPersistentVolumeSource",)


class V1CephFSPersistentVolumeSource(BaseModel):
    """Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.CephFSPersistentVolumeSource"
    )

    monitors: Annotated[
        list[str],
        Field(
            description="""monitors is Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it"""
        ),
    ]

    path: Annotated[
        str | None,
        Field(
            description="""path is Optional: Used as the mounted root, rather than the full Ceph tree, default is /""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    read_only: Annotated[
        bool | None,
        Field(
            alias="readOnly",
            description="""readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    secret_file: Annotated[
        str | None,
        Field(
            alias="secretFile",
            description="""secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    secret_ref: Annotated[
        V1SecretReference,
        Field(
            alias="secretRef",
            description="""secretRef is Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1SecretReference)),
    ] = V1SecretReference()

    user: Annotated[
        str | None,
        Field(
            description="""user is Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
