from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1GlusterfsVolumeSource",)


class V1GlusterfsVolumeSource(BaseConfiguredModel):
    """Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.GlusterfsVolumeSource"

    endpoints: Annotated[
        str,
        Field(
            description="""endpoints is the endpoint name that details Glusterfs topology."""
        ),
    ]

    path: Annotated[
        str,
        Field(
            description="""path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod"""
        ),
    ]

    read_only: Annotated[
        bool | None,
        Field(
            alias="readOnly",
            description="""readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
