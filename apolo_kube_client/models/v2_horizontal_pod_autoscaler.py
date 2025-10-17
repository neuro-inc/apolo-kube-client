from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v2_horizontal_pod_autoscaler_spec import V2HorizontalPodAutoscalerSpec
from .v2_horizontal_pod_autoscaler_status import V2HorizontalPodAutoscalerStatus

__all__ = ("V2HorizontalPodAutoscaler",)


class V2HorizontalPodAutoscaler(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    spec: V2HorizontalPodAutoscalerSpec = Field(
        default_factory=lambda: V2HorizontalPodAutoscalerSpec()
    )

    status: V2HorizontalPodAutoscalerStatus = Field(
        default_factory=lambda: V2HorizontalPodAutoscalerStatus()
    )
