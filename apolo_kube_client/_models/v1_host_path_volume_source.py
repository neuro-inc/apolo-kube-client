from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1HostPathVolumeSource",)


class V1HostPathVolumeSource(BaseModel):
    """Represents a host path mapped into a pod. Host path volumes do not support ownership management or SELinux relabeling."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.HostPathVolumeSource"

    path: Annotated[
        str,
        Field(
            description="""path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath"""
        ),
    ]

    type: Annotated[
        str | None,
        Field(
            description="""type for HostPath Volume Defaults to "" More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
