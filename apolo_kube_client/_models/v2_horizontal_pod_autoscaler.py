from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v2_horizontal_pod_autoscaler_spec import V2HorizontalPodAutoscalerSpec
from .v2_horizontal_pod_autoscaler_status import V2HorizontalPodAutoscalerStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V2HorizontalPodAutoscaler",)


class V2HorizontalPodAutoscaler(ResourceModel):
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
        V2HorizontalPodAutoscalerSpec,
        BeforeValidator(_default_if_none(V2HorizontalPodAutoscalerSpec)),
    ] = Field(default_factory=lambda: V2HorizontalPodAutoscalerSpec())

    status: Annotated[
        V2HorizontalPodAutoscalerStatus,
        BeforeValidator(_default_if_none(V2HorizontalPodAutoscalerStatus)),
    ] = Field(default_factory=lambda: V2HorizontalPodAutoscalerStatus())
