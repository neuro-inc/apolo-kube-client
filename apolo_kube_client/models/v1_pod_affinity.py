from pydantic import BaseModel, Field

from .v1_pod_affinity_term import V1PodAffinityTerm
from .v1_weighted_pod_affinity_term import V1WeightedPodAffinityTerm


class V1PodAffinity(BaseModel):
    preferred_during_scheduling_ignored_during_execution: (
        list[V1WeightedPodAffinityTerm] | None
    ) = Field(None, alias="preferredDuringSchedulingIgnoredDuringExecution")

    required_during_scheduling_ignored_during_execution: (
        list[V1PodAffinityTerm] | None
    ) = Field(None, alias="requiredDuringSchedulingIgnoredDuringExecution")
