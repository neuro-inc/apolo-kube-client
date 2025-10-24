from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ServiceAccountTokenProjection",)


class V1ServiceAccountTokenProjection(BaseModel):
    """ServiceAccountTokenProjection represents a projected service account token volume. This projection can be used to insert a service account token into the pods runtime filesystem for use against APIs (Kubernetes API Server or otherwise)."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.ServiceAccountTokenProjection"
    )

    audience: Annotated[
        str | None,
        Field(
            description="""audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    expiration_seconds: Annotated[
        int | None,
        Field(
            alias="expirationSeconds",
            description="""expirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    path: Annotated[
        str,
        Field(
            description="""path is the path relative to the mount point of the file to project the token into."""
        ),
    ]
