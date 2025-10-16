from __future__ import annotations

from pydantic import BaseModel, Field

from apolo_kube_client._typedefs import JsonType

from .v1_label_selector import V1LabelSelector

__all__ = ("V1PodDisruptionBudgetSpec",)


class V1PodDisruptionBudgetSpec(BaseModel):
    max_unavailable: JsonType | None = Field(None, alias="maxUnavailable")

    min_available: JsonType | None = Field(None, alias="minAvailable")

    selector: V1LabelSelector | None = Field(None, alias="selector")

    unhealthy_pod_eviction_policy: str | None = Field(
        None, alias="unhealthyPodEvictionPolicy"
    )
