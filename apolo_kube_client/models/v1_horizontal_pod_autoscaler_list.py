from pydantic import AliasChoices, Field
from .base import ListModel
from .v1_horizontal_pod_autoscaler import V1HorizontalPodAutoscaler
from .v1_list_meta import V1ListMeta

__all__ = ("V1HorizontalPodAutoscalerList",)


class V1HorizontalPodAutoscalerList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1HorizontalPodAutoscaler] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
