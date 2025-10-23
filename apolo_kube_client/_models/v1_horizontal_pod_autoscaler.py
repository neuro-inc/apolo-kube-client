from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
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
        exclude_if=_exclude_if,
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta(), exclude_if=_exclude_if)

    spec: Annotated[
        V1HorizontalPodAutoscalerSpec,
        BeforeValidator(_default_if_none(V1HorizontalPodAutoscalerSpec)),
    ] = Field(
        default_factory=lambda: V1HorizontalPodAutoscalerSpec(), exclude_if=_exclude_if
    )

    status: Annotated[
        V1HorizontalPodAutoscalerStatus,
        BeforeValidator(_default_if_none(V1HorizontalPodAutoscalerStatus)),
    ] = Field(
        default_factory=lambda: V1HorizontalPodAutoscalerStatus(),
        exclude_if=_exclude_if,
    )
