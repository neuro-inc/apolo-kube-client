from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_label_selector import V1LabelSelector
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1PodDisruptionBudgetSpec",)


class V1PodDisruptionBudgetSpec(BaseModel):
    max_unavailable: JsonType = Field(
        default_factory=lambda: {}, alias="maxUnavailable"
    )

    min_available: JsonType = Field(default_factory=lambda: {}, alias="minAvailable")

    selector: V1LabelSelector = Field(default_factory=lambda: V1LabelSelector())

    unhealthy_pod_eviction_policy: str | None = Field(
        default_factory=lambda: None, alias="unhealthyPodEvictionPolicy"
    )
