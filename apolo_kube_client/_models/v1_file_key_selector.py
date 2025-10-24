from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1FileKeySelector",)


class V1FileKeySelector(BaseModel):
    """FileKeySelector selects a key of the env file."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.FileKeySelector"

    key: Annotated[
        str,
        Field(
            description="""The key within the env file. An invalid key will prevent the pod from starting. The keys defined within a source may consist of any printable ASCII characters except '='. During Alpha stage of the EnvFiles feature gate, the key size is limited to 128 characters."""
        ),
    ]

    optional: Annotated[
        bool | None,
        Field(
            description="""Specify whether the file or its key must be defined. If the file or key does not exist, then the env var is not published. If optional is set to true and the specified key does not exist, the environment variable will not be set in the Pod's containers.

If optional is set to false and the specified key does not exist, an error will be returned during Pod creation.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    path: Annotated[
        str,
        Field(
            description="""The path within the volume from which to select the file. Must be relative and may not contain the '..' path or start with '..'."""
        ),
    ]

    volume_name: Annotated[
        str,
        Field(
            alias="volumeName",
            description="""The name of the volume mount containing the env file.""",
        ),
    ]
