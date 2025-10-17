from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_pod_affinity_term import V1PodAffinityTerm

__all__ = ("V1WeightedPodAffinityTerm",)


class V1WeightedPodAffinityTerm(BaseModel):
    pod_affinity_term: V1PodAffinityTerm = Field(
        default_factory=lambda: V1PodAffinityTerm(),
        serialization_alias="podAffinityTerm",
        validation_alias=AliasChoices("pod_affinity_term", "podAffinityTerm"),
    )

    weight: int | None = Field(default=None)
