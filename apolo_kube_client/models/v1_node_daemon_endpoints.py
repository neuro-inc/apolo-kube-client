from pydantic import BaseModel, Field

from .v1_daemon_endpoint import V1DaemonEndpoint


class V1NodeDaemonEndpoints(BaseModel):
    kubelet_endpoint: V1DaemonEndpoint | None = Field(None, alias="kubeletEndpoint")
