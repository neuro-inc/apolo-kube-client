from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_node_swap_status import V1NodeSwapStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NodeSystemInfo",)


class V1NodeSystemInfo(BaseModel):
    architecture: str | None = None

    boot_id: str | None = Field(
        default=None,
        serialization_alias="bootID",
        validation_alias=AliasChoices("boot_id", "bootID"),
    )

    container_runtime_version: str | None = Field(
        default=None,
        serialization_alias="containerRuntimeVersion",
        validation_alias=AliasChoices(
            "container_runtime_version", "containerRuntimeVersion"
        ),
    )

    kernel_version: str | None = Field(
        default=None,
        serialization_alias="kernelVersion",
        validation_alias=AliasChoices("kernel_version", "kernelVersion"),
    )

    kube_proxy_version: str | None = Field(
        default=None,
        serialization_alias="kubeProxyVersion",
        validation_alias=AliasChoices("kube_proxy_version", "kubeProxyVersion"),
    )

    kubelet_version: str | None = Field(
        default=None,
        serialization_alias="kubeletVersion",
        validation_alias=AliasChoices("kubelet_version", "kubeletVersion"),
    )

    machine_id: str | None = Field(
        default=None,
        serialization_alias="machineID",
        validation_alias=AliasChoices("machine_id", "machineID"),
    )

    operating_system: str | None = Field(
        default=None,
        serialization_alias="operatingSystem",
        validation_alias=AliasChoices("operating_system", "operatingSystem"),
    )

    os_image: str | None = Field(
        default=None,
        serialization_alias="osImage",
        validation_alias=AliasChoices("os_image", "osImage"),
    )

    swap: Annotated[
        V1NodeSwapStatus, BeforeValidator(_default_if_none(V1NodeSwapStatus))
    ] = Field(default_factory=lambda: V1NodeSwapStatus())

    system_uuid: str | None = Field(
        default=None,
        serialization_alias="systemUUID",
        validation_alias=AliasChoices("system_uuid", "systemUUID"),
    )
