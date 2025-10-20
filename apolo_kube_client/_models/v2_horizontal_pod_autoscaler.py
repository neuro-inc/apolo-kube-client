from pydantic import AliasChoices, Field
from .base import ResourceModel
from .v1_object_meta import V1ObjectMeta
from .v2_horizontal_pod_autoscaler_spec import V2HorizontalPodAutoscalerSpec
from .v2_horizontal_pod_autoscaler_status import V2HorizontalPodAutoscalerStatus

__all__ = ("V2HorizontalPodAutoscaler",)


class V2HorizontalPodAutoscaler(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V2HorizontalPodAutoscalerSpec = Field(
        default_factory=lambda: V2HorizontalPodAutoscalerSpec()
    )

    status: V2HorizontalPodAutoscalerStatus = Field(
        default_factory=lambda: V2HorizontalPodAutoscalerStatus()
    )
