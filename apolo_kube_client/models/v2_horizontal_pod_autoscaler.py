from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v2_horizontal_pod_autoscaler_spec import V2HorizontalPodAutoscalerSpec
from .v2_horizontal_pod_autoscaler_status import V2HorizontalPodAutoscalerStatus

__all__ = ("V2HorizontalPodAutoscaler",)


class V2HorizontalPodAutoscaler(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V2HorizontalPodAutoscalerSpec = Field(
        default_factory=lambda: V2HorizontalPodAutoscalerSpec(), alias="spec"
    )

    status: V2HorizontalPodAutoscalerStatus = Field(
        default_factory=lambda: V2HorizontalPodAutoscalerStatus(), alias="status"
    )
