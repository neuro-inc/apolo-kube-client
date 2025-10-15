from pydantic import BaseModel, Field

from .object import object
from .v1_label_selector import V1LabelSelector


class V1PodDisruptionBudgetSpec(BaseModel):
    max_unavailable: object | None = Field(None, alias="maxUnavailable")

    min_available: object | None = Field(None, alias="minAvailable")

    selector: V1LabelSelector | None = Field(None, alias="selector")

    unhealthy_pod_eviction_policy: str | None = Field(
        None, alias="unhealthyPodEvictionPolicy"
    )
