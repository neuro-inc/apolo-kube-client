from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_label_selector import V1LabelSelector
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1PodDisruptionBudgetSpec",)


class V1PodDisruptionBudgetSpec(BaseModel):
    max_unavailable: JsonType = Field(
        default={},
        serialization_alias="maxUnavailable",
        validation_alias=AliasChoices("max_unavailable", "maxUnavailable"),
    )

    min_available: JsonType = Field(
        default={},
        serialization_alias="minAvailable",
        validation_alias=AliasChoices("min_available", "minAvailable"),
    )

    selector: V1LabelSelector = Field(default_factory=lambda: V1LabelSelector())

    unhealthy_pod_eviction_policy: str | None = Field(
        default=None,
        serialization_alias="unhealthyPodEvictionPolicy",
        validation_alias=AliasChoices(
            "unhealthy_pod_eviction_policy", "unhealthyPodEvictionPolicy"
        ),
    )
