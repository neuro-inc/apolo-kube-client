from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_daemon_endpoint import V1DaemonEndpoint

__all__ = ("V1NodeDaemonEndpoints",)


class V1NodeDaemonEndpoints(BaseModel):
    kubelet_endpoint: V1DaemonEndpoint = Field(
        default_factory=lambda: V1DaemonEndpoint(), alias="kubeletEndpoint"
    )
