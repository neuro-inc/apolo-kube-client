from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_attached_volume import V1AttachedVolume
from .v1_container_image import V1ContainerImage
from .v1_node_address import V1NodeAddress
from .v1_node_condition import V1NodeCondition
from .v1_node_config_status import V1NodeConfigStatus
from .v1_node_daemon_endpoints import V1NodeDaemonEndpoints
from .v1_node_features import V1NodeFeatures
from .v1_node_runtime_handler import V1NodeRuntimeHandler
from .v1_node_system_info import V1NodeSystemInfo

__all__ = ("V1NodeStatus",)


class V1NodeStatus(BaseModel):
    addresses: list[V1NodeAddress] | None = Field(None, alias="addresses")

    allocatable: dict[str, str] | None = Field(None, alias="allocatable")

    capacity: dict[str, str] | None = Field(None, alias="capacity")

    conditions: list[V1NodeCondition] | None = Field(None, alias="conditions")

    config: V1NodeConfigStatus | None = Field(None, alias="config")

    daemon_endpoints: V1NodeDaemonEndpoints | None = Field(
        None, alias="daemonEndpoints"
    )

    features: V1NodeFeatures | None = Field(None, alias="features")

    images: list[V1ContainerImage] | None = Field(None, alias="images")

    node_info: V1NodeSystemInfo | None = Field(None, alias="nodeInfo")

    phase: str | None = Field(None, alias="phase")

    runtime_handlers: list[V1NodeRuntimeHandler] | None = Field(
        None, alias="runtimeHandlers"
    )

    volumes_attached: list[V1AttachedVolume] | None = Field(
        None, alias="volumesAttached"
    )

    volumes_in_use: list[str] | None = Field(None, alias="volumesInUse")
