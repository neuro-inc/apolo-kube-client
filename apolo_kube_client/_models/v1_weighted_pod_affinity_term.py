from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v1_pod_affinity_term import V1PodAffinityTerm
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1WeightedPodAffinityTerm",)


class V1WeightedPodAffinityTerm(BaseModel):
    pod_affinity_term: Annotated[
        V1PodAffinityTerm, BeforeValidator(_default_if_none(V1PodAffinityTerm))
    ] = Field(
        default_factory=lambda: V1PodAffinityTerm(),
        serialization_alias="podAffinityTerm",
        validation_alias=AliasChoices("pod_affinity_term", "podAffinityTerm"),
    )

    weight: int | None = None
