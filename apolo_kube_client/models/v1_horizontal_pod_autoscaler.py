from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_horizontal_pod_autoscaler_spec import V1HorizontalPodAutoscalerSpec
from .v1_horizontal_pod_autoscaler_status import V1HorizontalPodAutoscalerStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1HorizontalPodAutoscaler",)


class V1HorizontalPodAutoscaler(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1HorizontalPodAutoscalerSpec = Field(
        default_factory=lambda: V1HorizontalPodAutoscalerSpec()
    )

    status: V1HorizontalPodAutoscalerStatus = Field(
        default_factory=lambda: V1HorizontalPodAutoscalerStatus()
    )
