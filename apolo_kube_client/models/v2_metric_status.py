from pydantic import BaseModel, Field

from .v2_container_resource_metric_status import V2ContainerResourceMetricStatus
from .v2_external_metric_status import V2ExternalMetricStatus
from .v2_object_metric_status import V2ObjectMetricStatus
from .v2_pods_metric_status import V2PodsMetricStatus
from .v2_resource_metric_status import V2ResourceMetricStatus


class V2MetricStatus(BaseModel):
    container_resource: V2ContainerResourceMetricStatus | None = Field(
        None, alias="containerResource"
    )

    external: V2ExternalMetricStatus | None = Field(None, alias="external")

    object: V2ObjectMetricStatus | None = Field(None, alias="object")

    pods: V2PodsMetricStatus | None = Field(None, alias="pods")

    resource: V2ResourceMetricStatus | None = Field(None, alias="resource")

    type: str | None = Field(None, alias="type")
