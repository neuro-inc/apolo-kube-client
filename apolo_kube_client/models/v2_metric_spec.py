from __future__ import annotations

from pydantic import BaseModel, Field

from .v2_container_resource_metric_source import V2ContainerResourceMetricSource
from .v2_external_metric_source import V2ExternalMetricSource
from .v2_object_metric_source import V2ObjectMetricSource
from .v2_pods_metric_source import V2PodsMetricSource
from .v2_resource_metric_source import V2ResourceMetricSource

__all__ = ("V2MetricSpec",)


class V2MetricSpec(BaseModel):
    container_resource: V2ContainerResourceMetricSource | None = Field(
        None, alias="containerResource"
    )

    external: V2ExternalMetricSource | None = Field(None, alias="external")

    object: V2ObjectMetricSource | None = Field(None, alias="object")

    pods: V2PodsMetricSource | None = Field(None, alias="pods")

    resource: V2ResourceMetricSource | None = Field(None, alias="resource")

    type: str | None = Field(None, alias="type")
