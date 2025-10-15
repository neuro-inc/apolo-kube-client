from pydantic import BaseModel, Field

from .v1_cross_version_object_reference import V1CrossVersionObjectReference


class V1HorizontalPodAutoscalerSpec(BaseModel):
    max_replicas: int | None = Field(None, alias="maxReplicas")

    min_replicas: int | None = Field(None, alias="minReplicas")

    scale_target_ref: V1CrossVersionObjectReference | None = Field(
        None, alias="scaleTargetRef"
    )

    target_cpu_utilization_percentage: int | None = Field(
        None, alias="targetCPUUtilizationPercentage"
    )
