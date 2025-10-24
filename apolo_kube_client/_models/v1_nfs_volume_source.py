from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1NFSVolumeSource",)


class V1NFSVolumeSource(BaseModel):
    """Represents an NFS mount that lasts the lifetime of a pod. NFS volumes do not support ownership management or SELinux relabeling."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.NFSVolumeSource"

    path: Annotated[
        str,
        Field(
            description="""path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs"""
        ),
    ]

    read_only: Annotated[
        bool | None,
        Field(
            alias="readOnly",
            description="""readOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    server: Annotated[
        str,
        Field(
            description="""server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs"""
        ),
    ]
