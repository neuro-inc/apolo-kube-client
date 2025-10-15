from pydantic import BaseModel, Field

from .v1_horizontal_pod_autoscaler_spec import V1HorizontalPodAutoscalerSpec
from .v1_horizontal_pod_autoscaler_status import V1HorizontalPodAutoscalerStatus
from .v1_object_meta import V1ObjectMeta


class V1HorizontalPodAutoscaler(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1HorizontalPodAutoscalerSpec | None = Field(None, alias="spec")

    status: V1HorizontalPodAutoscalerStatus | None = Field(None, alias="status")
