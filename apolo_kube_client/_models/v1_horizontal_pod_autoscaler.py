from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
from .v1_horizontal_pod_autoscaler_spec import V1HorizontalPodAutoscalerSpec
from .v1_horizontal_pod_autoscaler_status import V1HorizontalPodAutoscalerStatus
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1HorizontalPodAutoscaler",)


class V1HorizontalPodAutoscaler(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[
        V1HorizontalPodAutoscalerSpec,
        BeforeValidator(_default_if_none(V1HorizontalPodAutoscalerSpec)),
    ] = Field(default_factory=lambda: V1HorizontalPodAutoscalerSpec())

    status: Annotated[
        V1HorizontalPodAutoscalerStatus,
        BeforeValidator(_default_if_none(V1HorizontalPodAutoscalerStatus)),
    ] = Field(default_factory=lambda: V1HorizontalPodAutoscalerStatus())
