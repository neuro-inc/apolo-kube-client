from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_pod_affinity_term import V1PodAffinityTerm

__all__ = ("V1WeightedPodAffinityTerm",)


class V1WeightedPodAffinityTerm(BaseModel):
    """The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s)"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.WeightedPodAffinityTerm"

    pod_affinity_term: Annotated[
        V1PodAffinityTerm,
        Field(
            alias="podAffinityTerm",
            description="""Required. A pod affinity term, associated with the corresponding weight.""",
        ),
    ]

    weight: Annotated[
        int,
        Field(
            description="""weight associated with matching the corresponding podAffinityTerm, in the range 1-100."""
        ),
    ]
