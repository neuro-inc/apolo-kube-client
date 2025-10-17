from pydantic import AliasChoices, BaseModel, Field
from .v1_pod_affinity_term import V1PodAffinityTerm
from .v1_weighted_pod_affinity_term import V1WeightedPodAffinityTerm

__all__ = ("V1PodAffinity",)


class V1PodAffinity(BaseModel):
    preferred_during_scheduling_ignored_during_execution: list[
        V1WeightedPodAffinityTerm
    ] = Field(
        default=[],
        serialization_alias="preferredDuringSchedulingIgnoredDuringExecution",
        validation_alias=AliasChoices(
            "preferred_during_scheduling_ignored_during_execution",
            "preferredDuringSchedulingIgnoredDuringExecution",
        ),
    )

    required_during_scheduling_ignored_during_execution: list[V1PodAffinityTerm] = (
        Field(
            default=[],
            serialization_alias="requiredDuringSchedulingIgnoredDuringExecution",
            validation_alias=AliasChoices(
                "required_during_scheduling_ignored_during_execution",
                "requiredDuringSchedulingIgnoredDuringExecution",
            ),
        )
    )
