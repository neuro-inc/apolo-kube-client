from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_horizontal_pod_autoscaler import V1HorizontalPodAutoscaler
from .v1_list_meta import V1ListMeta

__all__ = ("V1HorizontalPodAutoscalerList",)


class V1HorizontalPodAutoscalerList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1HorizontalPodAutoscaler] = Field(default_factory=lambda: [])

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
