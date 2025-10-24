from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1KeyToPath",)


class V1KeyToPath(BaseModel):
    """Maps a string key to a path within a volume."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.KeyToPath"

    key: Annotated[str, Field(description="""key is the key to project.""")]

    mode: Annotated[
        int | None,
        Field(
            description="""mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    path: Annotated[
        str,
        Field(
            description="""path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'."""
        ),
    ]
