from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_pod_affinity_term import V1PodAffinityTerm
from .v1_weighted_pod_affinity_term import V1WeightedPodAffinityTerm
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PodAffinity",)


class V1PodAffinity(BaseModel):
    preferred_during_scheduling_ignored_during_execution: Annotated[
        list[V1WeightedPodAffinityTerm], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="preferredDuringSchedulingIgnoredDuringExecution",
        validation_alias=AliasChoices(
            "preferred_during_scheduling_ignored_during_execution",
            "preferredDuringSchedulingIgnoredDuringExecution",
        ),
    )

    required_during_scheduling_ignored_during_execution: Annotated[
        list[V1PodAffinityTerm], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="requiredDuringSchedulingIgnoredDuringExecution",
        validation_alias=AliasChoices(
            "required_during_scheduling_ignored_during_execution",
            "requiredDuringSchedulingIgnoredDuringExecution",
        ),
    )
