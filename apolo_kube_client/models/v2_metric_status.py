from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v2_container_resource_metric_status import V2ContainerResourceMetricStatus
from .v2_external_metric_status import V2ExternalMetricStatus
from .v2_object_metric_status import V2ObjectMetricStatus
from .v2_pods_metric_status import V2PodsMetricStatus
from .v2_resource_metric_status import V2ResourceMetricStatus

__all__ = ("V2MetricStatus",)


class V2MetricStatus(BaseModel):
    container_resource: V2ContainerResourceMetricStatus = Field(
        default_factory=lambda: V2ContainerResourceMetricStatus(),
        serialization_alias="containerResource",
        validation_alias=AliasChoices("container_resource", "containerResource"),
    )

    external: V2ExternalMetricStatus = Field(
        default_factory=lambda: V2ExternalMetricStatus()
    )

    object: V2ObjectMetricStatus = Field(default_factory=lambda: V2ObjectMetricStatus())

    pods: V2PodsMetricStatus = Field(default_factory=lambda: V2PodsMetricStatus())

    resource: V2ResourceMetricStatus = Field(
        default_factory=lambda: V2ResourceMetricStatus()
    )

    type: str | None = Field(default=None)
