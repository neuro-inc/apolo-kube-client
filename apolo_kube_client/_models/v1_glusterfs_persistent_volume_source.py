from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1GlusterfsPersistentVolumeSource",)


class V1GlusterfsPersistentVolumeSource(BaseModel):
    """Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.GlusterfsPersistentVolumeSource"
    )

    endpoints: Annotated[
        str,
        Field(
            description="""endpoints is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod"""
        ),
    ]

    endpoints_namespace: Annotated[
        str | None,
        Field(
            alias="endpointsNamespace",
            description="""endpointsNamespace is the namespace that contains Glusterfs endpoint. If this field is empty, the EndpointNamespace defaults to the same namespace as the bound PVC. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

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
