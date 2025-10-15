from pydantic import BaseModel, Field

from .v1_horizontal_pod_autoscaler import V1HorizontalPodAutoscaler
from .v1_list_meta import V1ListMeta


class V1HorizontalPodAutoscalerList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1HorizontalPodAutoscaler] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
