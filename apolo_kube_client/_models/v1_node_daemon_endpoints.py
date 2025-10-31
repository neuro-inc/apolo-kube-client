from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_daemon_endpoint import V1DaemonEndpoint

__all__ = ("V1NodeDaemonEndpoints",)


class V1NodeDaemonEndpoints(BaseModel):
    """NodeDaemonEndpoints lists ports opened by daemons running on the Node."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.NodeDaemonEndpoints"

    kubelet_endpoint: Annotated[
        V1DaemonEndpoint | None,
        Field(
            alias="kubeletEndpoint",
            description="""Endpoint on which Kubelet is listening.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
