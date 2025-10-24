from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1SeccompProfile",)


class V1SeccompProfile(BaseModel):
    """SeccompProfile defines a pod/container's seccomp profile settings. Only one profile source may be set."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.SeccompProfile"

    localhost_profile: Annotated[
        str | None,
        Field(
            alias="localhostProfile",
            description="""localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet's configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    type: Annotated[
        str,
        Field(
            description="""type indicates which kind of seccomp profile will be applied. Valid options are:

Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied."""
        ),
    ]
