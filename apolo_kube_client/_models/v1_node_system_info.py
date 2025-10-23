from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_node_swap_status import V1NodeSwapStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NodeSystemInfo",)


class V1NodeSystemInfo(BaseModel):
    architecture: str | None = Field(default=None, exclude_if=_exclude_if)

    boot_id: str | None = Field(
        default=None,
        serialization_alias="bootID",
        validation_alias=AliasChoices("boot_id", "bootID"),
        exclude_if=_exclude_if,
    )

    container_runtime_version: str | None = Field(
        default=None,
        serialization_alias="containerRuntimeVersion",
        validation_alias=AliasChoices(
            "container_runtime_version", "containerRuntimeVersion"
        ),
        exclude_if=_exclude_if,
    )

    kernel_version: str | None = Field(
        default=None,
        serialization_alias="kernelVersion",
        validation_alias=AliasChoices("kernel_version", "kernelVersion"),
        exclude_if=_exclude_if,
    )

    kube_proxy_version: str | None = Field(
        default=None,
        serialization_alias="kubeProxyVersion",
        validation_alias=AliasChoices("kube_proxy_version", "kubeProxyVersion"),
        exclude_if=_exclude_if,
    )

    kubelet_version: str | None = Field(
        default=None,
        serialization_alias="kubeletVersion",
        validation_alias=AliasChoices("kubelet_version", "kubeletVersion"),
        exclude_if=_exclude_if,
    )

    machine_id: str | None = Field(
        default=None,
        serialization_alias="machineID",
        validation_alias=AliasChoices("machine_id", "machineID"),
        exclude_if=_exclude_if,
    )

    operating_system: str | None = Field(
        default=None,
        serialization_alias="operatingSystem",
        validation_alias=AliasChoices("operating_system", "operatingSystem"),
        exclude_if=_exclude_if,
    )

    os_image: str | None = Field(
        default=None,
        serialization_alias="osImage",
        validation_alias=AliasChoices("os_image", "osImage"),
        exclude_if=_exclude_if,
    )

    swap: Annotated[
        V1NodeSwapStatus, BeforeValidator(_default_if_none(V1NodeSwapStatus))
    ] = Field(default_factory=lambda: V1NodeSwapStatus(), exclude_if=_exclude_if)

    system_uuid: str | None = Field(
        default=None,
        serialization_alias="systemUUID",
        validation_alias=AliasChoices("system_uuid", "systemUUID"),
        exclude_if=_exclude_if,
    )
