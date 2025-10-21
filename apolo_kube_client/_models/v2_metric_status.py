from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v2_container_resource_metric_status import V2ContainerResourceMetricStatus
from .v2_external_metric_status import V2ExternalMetricStatus
from .v2_object_metric_status import V2ObjectMetricStatus
from .v2_pods_metric_status import V2PodsMetricStatus
from .v2_resource_metric_status import V2ResourceMetricStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V2MetricStatus",)


class V2MetricStatus(BaseModel):
    container_resource: Annotated[
        V2ContainerResourceMetricStatus,
        BeforeValidator(_default_if_none(V2ContainerResourceMetricStatus)),
    ] = Field(
        default_factory=lambda: V2ContainerResourceMetricStatus(),
        serialization_alias="containerResource",
        validation_alias=AliasChoices("container_resource", "containerResource"),
    )

    external: Annotated[
        V2ExternalMetricStatus,
        BeforeValidator(_default_if_none(V2ExternalMetricStatus)),
    ] = Field(default_factory=lambda: V2ExternalMetricStatus())

    object: Annotated[
        V2ObjectMetricStatus, BeforeValidator(_default_if_none(V2ObjectMetricStatus))
    ] = Field(default_factory=lambda: V2ObjectMetricStatus())

    pods: Annotated[
        V2PodsMetricStatus, BeforeValidator(_default_if_none(V2PodsMetricStatus))
    ] = Field(default_factory=lambda: V2PodsMetricStatus())

    resource: Annotated[
        V2ResourceMetricStatus,
        BeforeValidator(_default_if_none(V2ResourceMetricStatus)),
    ] = Field(default_factory=lambda: V2ResourceMetricStatus())

    type: str | None = None
