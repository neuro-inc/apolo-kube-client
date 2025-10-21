from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_attached_volume import V1AttachedVolume
from .v1_container_image import V1ContainerImage
from .v1_node_address import V1NodeAddress
from .v1_node_condition import V1NodeCondition
from .v1_node_config_status import V1NodeConfigStatus
from .v1_node_daemon_endpoints import V1NodeDaemonEndpoints
from .v1_node_features import V1NodeFeatures
from .v1_node_runtime_handler import V1NodeRuntimeHandler
from .v1_node_system_info import V1NodeSystemInfo
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NodeStatus",)


class V1NodeStatus(BaseModel):
    addresses: list[V1NodeAddress] = []

    allocatable: dict[str, str] = {}

    capacity: dict[str, str] = {}

    conditions: list[V1NodeCondition] = []

    config: Annotated[
        V1NodeConfigStatus, BeforeValidator(_default_if_none(V1NodeConfigStatus))
    ] = Field(default_factory=lambda: V1NodeConfigStatus())

    daemon_endpoints: Annotated[
        V1NodeDaemonEndpoints, BeforeValidator(_default_if_none(V1NodeDaemonEndpoints))
    ] = Field(
        default_factory=lambda: V1NodeDaemonEndpoints(),
        serialization_alias="daemonEndpoints",
        validation_alias=AliasChoices("daemon_endpoints", "daemonEndpoints"),
    )

    features: Annotated[
        V1NodeFeatures, BeforeValidator(_default_if_none(V1NodeFeatures))
    ] = Field(default_factory=lambda: V1NodeFeatures())

    images: list[V1ContainerImage] = []

    node_info: Annotated[
        V1NodeSystemInfo, BeforeValidator(_default_if_none(V1NodeSystemInfo))
    ] = Field(
        default_factory=lambda: V1NodeSystemInfo(),
        serialization_alias="nodeInfo",
        validation_alias=AliasChoices("node_info", "nodeInfo"),
    )

    phase: str | None = None

    runtime_handlers: list[V1NodeRuntimeHandler] = Field(
        default=[],
        serialization_alias="runtimeHandlers",
        validation_alias=AliasChoices("runtime_handlers", "runtimeHandlers"),
    )

    volumes_attached: list[V1AttachedVolume] = Field(
        default=[],
        serialization_alias="volumesAttached",
        validation_alias=AliasChoices("volumes_attached", "volumesAttached"),
    )

    volumes_in_use: list[str] = Field(
        default=[],
        serialization_alias="volumesInUse",
        validation_alias=AliasChoices("volumes_in_use", "volumesInUse"),
    )
