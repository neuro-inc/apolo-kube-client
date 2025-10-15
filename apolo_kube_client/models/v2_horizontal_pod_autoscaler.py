from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v2_horizontal_pod_autoscaler_spec import V2HorizontalPodAutoscalerSpec
from .v2_horizontal_pod_autoscaler_status import V2HorizontalPodAutoscalerStatus


class V2HorizontalPodAutoscaler(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V2HorizontalPodAutoscalerSpec | None = Field(None, alias="spec")

    status: V2HorizontalPodAutoscalerStatus | None = Field(None, alias="status")
