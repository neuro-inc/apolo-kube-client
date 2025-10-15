from datetime import datetime

from pydantic import BaseModel, Field

from .v2_horizontal_pod_autoscaler_condition import V2HorizontalPodAutoscalerCondition
from .v2_metric_status import V2MetricStatus


class V2HorizontalPodAutoscalerStatus(BaseModel):
    conditions: list[V2HorizontalPodAutoscalerCondition] | None = Field(
        None, alias="conditions"
    )

    current_metrics: list[V2MetricStatus] | None = Field(None, alias="currentMetrics")

    current_replicas: int | None = Field(None, alias="currentReplicas")

    desired_replicas: int | None = Field(None, alias="desiredReplicas")

    last_scale_time: datetime | None = Field(None, alias="lastScaleTime")

    observed_generation: int | None = Field(None, alias="observedGeneration")
