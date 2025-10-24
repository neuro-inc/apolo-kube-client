from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1VolumeMount",)


class V1VolumeMount(BaseModel):
    """VolumeMount describes a mounting of a Volume within a container."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.VolumeMount"

    mount_path: Annotated[
        str,
        Field(
            alias="mountPath",
            description="""Path within the container at which the volume should be mounted.  Must not contain ':'.""",
        ),
    ]

    mount_propagation: Annotated[
        str | None,
        Field(
            alias="mountPropagation",
            description="""mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. When RecursiveReadOnly is set to IfPossible or to Enabled, MountPropagation must be None or unspecified (which defaults to None).""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    name: Annotated[str, Field(description="""This must match the Name of a Volume.""")]

    read_only: Annotated[
        bool | None,
        Field(
            alias="readOnly",
            description="""Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    recursive_read_only: Annotated[
        str | None,
        Field(
            alias="recursiveReadOnly",
            description="""RecursiveReadOnly specifies whether read-only mounts should be handled recursively.

If ReadOnly is false, this field has no meaning and must be unspecified.

If ReadOnly is true, and this field is set to Disabled, the mount is not made recursively read-only.  If this field is set to IfPossible, the mount is made recursively read-only, if it is supported by the container runtime.  If this field is set to Enabled, the mount is made recursively read-only if it is supported by the container runtime, otherwise the pod will not be started and an error will be generated to indicate the reason.

If this field is set to IfPossible or Enabled, MountPropagation must be set to None (or be unspecified, which defaults to None).

If this field is not specified, it is treated as an equivalent of Disabled.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    sub_path: Annotated[
        str | None,
        Field(
            alias="subPath",
            description="""Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root).""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    sub_path_expr: Annotated[
        str | None,
        Field(
            alias="subPathExpr",
            description="""Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). SubPathExpr and SubPath are mutually exclusive.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
