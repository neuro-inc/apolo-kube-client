from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v2_horizontal_pod_autoscaler import V2HorizontalPodAutoscaler

__all__ = ("V2HorizontalPodAutoscalerList",)


class V2HorizontalPodAutoscalerList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V2HorizontalPodAutoscaler] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
