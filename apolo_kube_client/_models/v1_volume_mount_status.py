from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1VolumeMountStatus",)


class V1VolumeMountStatus(BaseModel):
    """VolumeMountStatus shows status of volume mounts."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.VolumeMountStatus"

    mount_path: Annotated[
        str,
        Field(
            alias="mountPath",
            description="""MountPath corresponds to the original VolumeMount.""",
        ),
    ]

    name: Annotated[
        str,
        Field(
            description="""Name corresponds to the name of the original VolumeMount."""
        ),
    ]

    read_only: Annotated[
        bool | None,
        Field(
            alias="readOnly",
            description="""ReadOnly corresponds to the original VolumeMount.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    recursive_read_only: Annotated[
        str | None,
        Field(
            alias="recursiveReadOnly",
            description="""RecursiveReadOnly must be set to Disabled, Enabled, or unspecified (for non-readonly mounts). An IfPossible value in the original VolumeMount must be translated to Disabled or Enabled, depending on the mount result.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
