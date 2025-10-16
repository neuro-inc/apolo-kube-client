from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_pod_affinity_term import V1PodAffinityTerm

__all__ = ("V1WeightedPodAffinityTerm",)


class V1WeightedPodAffinityTerm(BaseModel):
    pod_affinity_term: V1PodAffinityTerm | None = Field(None, alias="podAffinityTerm")

    weight: int | None = Field(None, alias="weight")
