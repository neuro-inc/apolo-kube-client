from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_horizontal_pod_autoscaler import V1HorizontalPodAutoscaler
from .v1_list_meta import V1ListMeta

__all__ = ("V1HorizontalPodAutoscalerList",)


class V1HorizontalPodAutoscalerList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1HorizontalPodAutoscaler] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
