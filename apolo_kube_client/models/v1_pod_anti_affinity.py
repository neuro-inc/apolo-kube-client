from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_pod_affinity_term import V1PodAffinityTerm
from .v1_weighted_pod_affinity_term import V1WeightedPodAffinityTerm

__all__ = ("V1PodAntiAffinity",)


class V1PodAntiAffinity(BaseModel):
    preferred_during_scheduling_ignored_during_execution: list[
        V1WeightedPodAffinityTerm
    ] = Field(
        default_factory=lambda: [],
        alias="preferredDuringSchedulingIgnoredDuringExecution",
    )

    required_during_scheduling_ignored_during_execution: list[V1PodAffinityTerm] = (
        Field(
            default_factory=lambda: [],
            alias="requiredDuringSchedulingIgnoredDuringExecution",
        )
    )
