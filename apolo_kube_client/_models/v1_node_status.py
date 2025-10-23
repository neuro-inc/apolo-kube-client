from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
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
    addresses: Annotated[
        list[V1NodeAddress], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    allocatable: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = Field(default={}, exclude_if=_exclude_if)

    capacity: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = (
        Field(default={}, exclude_if=_exclude_if)
    )

    conditions: Annotated[
        list[V1NodeCondition], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    config: Annotated[
        V1NodeConfigStatus, BeforeValidator(_default_if_none(V1NodeConfigStatus))
    ] = Field(default_factory=lambda: V1NodeConfigStatus(), exclude_if=_exclude_if)

    daemon_endpoints: Annotated[
        V1NodeDaemonEndpoints, BeforeValidator(_default_if_none(V1NodeDaemonEndpoints))
    ] = Field(
        default_factory=lambda: V1NodeDaemonEndpoints(),
        serialization_alias="daemonEndpoints",
        validation_alias=AliasChoices("daemon_endpoints", "daemonEndpoints"),
        exclude_if=_exclude_if,
    )

    features: Annotated[
        V1NodeFeatures, BeforeValidator(_default_if_none(V1NodeFeatures))
    ] = Field(default_factory=lambda: V1NodeFeatures(), exclude_if=_exclude_if)

    images: Annotated[
        list[V1ContainerImage], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    node_info: Annotated[
        V1NodeSystemInfo, BeforeValidator(_default_if_none(V1NodeSystemInfo))
    ] = Field(
        default_factory=lambda: V1NodeSystemInfo(),
        serialization_alias="nodeInfo",
        validation_alias=AliasChoices("node_info", "nodeInfo"),
        exclude_if=_exclude_if,
    )

    phase: str | None = Field(default=None, exclude_if=_exclude_if)

    runtime_handlers: Annotated[
        list[V1NodeRuntimeHandler], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="runtimeHandlers",
        validation_alias=AliasChoices("runtime_handlers", "runtimeHandlers"),
        exclude_if=_exclude_if,
    )

    volumes_attached: Annotated[
        list[V1AttachedVolume], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="volumesAttached",
        validation_alias=AliasChoices("volumes_attached", "volumesAttached"),
        exclude_if=_exclude_if,
    )

    volumes_in_use: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="volumesInUse",
            validation_alias=AliasChoices("volumes_in_use", "volumesInUse"),
            exclude_if=_exclude_if,
        )
    )
