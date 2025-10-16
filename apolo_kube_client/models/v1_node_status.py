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
    addresses: list[V1NodeAddress] = Field(
        default_factory=lambda: [], alias="addresses"
    )

    allocatable: dict[str, str] = Field(default_factory=lambda: {}, alias="allocatable")

    capacity: dict[str, str] = Field(default_factory=lambda: {}, alias="capacity")

    conditions: list[V1NodeCondition] = Field(
        default_factory=lambda: [], alias="conditions"
    )

    config: V1NodeConfigStatus = Field(
        default_factory=lambda: V1NodeConfigStatus(), alias="config"
    )

    daemon_endpoints: V1NodeDaemonEndpoints = Field(
        default_factory=lambda: V1NodeDaemonEndpoints(), alias="daemonEndpoints"
    )

    features: V1NodeFeatures = Field(
        default_factory=lambda: V1NodeFeatures(), alias="features"
    )

    images: list[V1ContainerImage] = Field(default_factory=lambda: [], alias="images")

    node_info: V1NodeSystemInfo = Field(
        default_factory=lambda: V1NodeSystemInfo(), alias="nodeInfo"
    )

    phase: str | None = Field(default_factory=lambda: None, alias="phase")

    runtime_handlers: list[V1NodeRuntimeHandler] = Field(
        default_factory=lambda: [], alias="runtimeHandlers"
    )

    volumes_attached: list[V1AttachedVolume] = Field(
        default_factory=lambda: [], alias="volumesAttached"
    )

    volumes_in_use: list[str] = Field(default_factory=lambda: [], alias="volumesInUse")
