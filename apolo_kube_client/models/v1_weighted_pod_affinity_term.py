from pydantic import BaseModel, Field

from .v1_pod_affinity_term import V1PodAffinityTerm


class V1WeightedPodAffinityTerm(BaseModel):
    pod_affinity_term: V1PodAffinityTerm | None = Field(None, alias="podAffinityTerm")

    weight: int | None = Field(None, alias="weight")
