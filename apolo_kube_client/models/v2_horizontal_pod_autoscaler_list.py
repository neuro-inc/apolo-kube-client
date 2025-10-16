from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v2_horizontal_pod_autoscaler import V2HorizontalPodAutoscaler

__all__ = ("V2HorizontalPodAutoscalerList",)


class V2HorizontalPodAutoscalerList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V2HorizontalPodAutoscaler] = Field(
        default_factory=lambda: [], alias="items"
    )

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta(), alias="metadata")
