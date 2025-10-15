from pydantic import BaseModel, Field


class V1NodeSystemInfo(BaseModel):
    architecture: str | None = Field(None, alias="architecture")

    boot_id: str | None = Field(None, alias="bootID")

    container_runtime_version: str | None = Field(None, alias="containerRuntimeVersion")

    kernel_version: str | None = Field(None, alias="kernelVersion")

    kube_proxy_version: str | None = Field(None, alias="kubeProxyVersion")

    kubelet_version: str | None = Field(None, alias="kubeletVersion")

    machine_id: str | None = Field(None, alias="machineID")

    operating_system: str | None = Field(None, alias="operatingSystem")

    os_image: str | None = Field(None, alias="osImage")

    system_uuid: str | None = Field(None, alias="systemUUID")
