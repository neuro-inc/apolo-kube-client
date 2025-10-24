from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_condition import V1Condition
from datetime import datetime
from pydantic import BeforeValidator

__all__ = ("V1PodDisruptionBudgetStatus",)


class V1PodDisruptionBudgetStatus(BaseModel):
    """PodDisruptionBudgetStatus represents information about the status of a PodDisruptionBudget. Status may trail the actual state of a system."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.policy.v1.PodDisruptionBudgetStatus"
    )

    conditions: Annotated[
        list[V1Condition],
        Field(
            description="""Conditions contain conditions for PDB. The disruption controller sets the DisruptionAllowed condition. The following are known values for the reason field (additional reasons could be added in the future): - SyncFailed: The controller encountered an error and wasn't able to compute
              the number of allowed disruptions. Therefore no disruptions are
              allowed and the status of the condition will be False.
- InsufficientPods: The number of pods are either at or below the number
                    required by the PodDisruptionBudget. No disruptions are
                    allowed and the status of the condition will be False.
- SufficientPods: There are more pods than required by the PodDisruptionBudget.
                  The condition will be True, and the number of allowed
                  disruptions are provided by the disruptionsAllowed property.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    current_healthy: Annotated[
        int,
        Field(alias="currentHealthy", description="""current number of healthy pods"""),
    ]

    desired_healthy: Annotated[
        int,
        Field(
            alias="desiredHealthy",
            description="""minimum desired number of healthy pods""",
        ),
    ]

    disrupted_pods: Annotated[
        dict[str, datetime],
        Field(
            alias="disruptedPods",
            description="""DisruptedPods contains information about pods whose eviction was processed by the API server eviction subresource handler but has not yet been observed by the PodDisruptionBudget controller. A pod will be in this map from the time when the API server processed the eviction request to the time when the pod is seen by PDB controller as having been marked for deletion (or after a timeout). The key in the map is the name of the pod and the value is the time when the API server processed the eviction request. If the deletion didn't occur and a pod is still there it will be removed from the list automatically by PodDisruptionBudget controller after some time. If everything goes smooth this map should be empty for the most of the time. Large number of entries in the map may indicate problems with pod deletions.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    disruptions_allowed: Annotated[
        int,
        Field(
            alias="disruptionsAllowed",
            description="""Number of pod disruptions that are currently allowed.""",
        ),
    ]

    expected_pods: Annotated[
        int,
        Field(
            alias="expectedPods",
            description="""total number of pods counted by this disruption budget""",
        ),
    ]

    observed_generation: Annotated[
        int | None,
        Field(
            alias="observedGeneration",
            description="""Most recent generation observed when updating this PDB status. DisruptionsAllowed and other status information is valid only if observedGeneration equals to PDB's object generation.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
