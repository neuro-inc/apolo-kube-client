from __future__ import annotations
from pydantic import BaseModel, Field
from .v2_container_resource_metric_source import V2ContainerResourceMetricSource
from .v2_external_metric_source import V2ExternalMetricSource
from .v2_object_metric_source import V2ObjectMetricSource
from .v2_pods_metric_source import V2PodsMetricSource
from .v2_resource_metric_source import V2ResourceMetricSource

__all__ = ("V2MetricSpec",)


class V2MetricSpec(BaseModel):
    container_resource: V2ContainerResourceMetricSource = Field(
        default_factory=lambda: V2ContainerResourceMetricSource(),
        alias="containerResource",
    )

    external: V2ExternalMetricSource = Field(
        default_factory=lambda: V2ExternalMetricSource()
    )

    object: V2ObjectMetricSource = Field(default_factory=lambda: V2ObjectMetricSource())

    pods: V2PodsMetricSource = Field(default_factory=lambda: V2PodsMetricSource())

    resource: V2ResourceMetricSource = Field(
        default_factory=lambda: V2ResourceMetricSource()
    )

    type: str | None = Field(default_factory=lambda: None)
