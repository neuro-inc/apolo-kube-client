from pydantic import AliasChoices, BaseModel, Field
from .v1_daemon_endpoint import V1DaemonEndpoint

__all__ = ("V1NodeDaemonEndpoints",)


class V1NodeDaemonEndpoints(BaseModel):
    kubelet_endpoint: V1DaemonEndpoint = Field(
        default_factory=lambda: V1DaemonEndpoint(),
        serialization_alias="kubeletEndpoint",
        validation_alias=AliasChoices("kubelet_endpoint", "kubeletEndpoint"),
    )
