from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v2_horizontal_pod_autoscaler import V2HorizontalPodAutoscaler


class V2HorizontalPodAutoscalerList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V2HorizontalPodAutoscaler] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
