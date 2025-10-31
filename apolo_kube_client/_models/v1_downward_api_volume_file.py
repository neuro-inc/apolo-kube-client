from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_object_field_selector import V1ObjectFieldSelector
from .v1_resource_field_selector import V1ResourceFieldSelector

__all__ = ("V1DownwardAPIVolumeFile",)


class V1DownwardAPIVolumeFile(BaseModel):
    """DownwardAPIVolumeFile represents information to create the file containing the pod field"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.DownwardAPIVolumeFile"

    field_ref: Annotated[
        V1ObjectFieldSelector | None,
        Field(
            alias="fieldRef",
            description="""Required: Selects a field of the pod: only annotations, labels, name, namespace and uid are supported.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    mode: Annotated[
        int | None,
        Field(
            description="""Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    path: Annotated[
        str,
        Field(
            description="""Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'"""
        ),
    ]

    resource_field_ref: Annotated[
        V1ResourceFieldSelector | None,
        Field(
            alias="resourceFieldRef",
            description="""Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
