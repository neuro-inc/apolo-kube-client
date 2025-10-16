from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_node_swap_status import V1NodeSwapStatus

__all__ = ("V1NodeSystemInfo",)


class V1NodeSystemInfo(BaseModel):
    architecture: str | None = Field(default_factory=lambda: None, alias="architecture")

    boot_id: str | None = Field(default_factory=lambda: None, alias="bootID")

    container_runtime_version: str | None = Field(
        default_factory=lambda: None, alias="containerRuntimeVersion"
    )

    kernel_version: str | None = Field(
        default_factory=lambda: None, alias="kernelVersion"
    )

    kube_proxy_version: str | None = Field(
        default_factory=lambda: None, alias="kubeProxyVersion"
    )

    kubelet_version: str | None = Field(
        default_factory=lambda: None, alias="kubeletVersion"
    )

    machine_id: str | None = Field(default_factory=lambda: None, alias="machineID")

    operating_system: str | None = Field(
        default_factory=lambda: None, alias="operatingSystem"
    )

    os_image: str | None = Field(default_factory=lambda: None, alias="osImage")

    swap: V1NodeSwapStatus = Field(
        default_factory=lambda: V1NodeSwapStatus(), alias="swap"
    )

    system_uuid: str | None = Field(default_factory=lambda: None, alias="systemUUID")
