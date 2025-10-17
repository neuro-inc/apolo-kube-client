from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_replica_set_condition import V1ReplicaSetCondition

__all__ = ("V1ReplicaSetStatus",)


class V1ReplicaSetStatus(BaseModel):
    available_replicas: int | None = Field(
        default_factory=lambda: None, alias="availableReplicas"
    )

    conditions: list[V1ReplicaSetCondition] = Field(default_factory=lambda: [])

    fully_labeled_replicas: int | None = Field(
        default_factory=lambda: None, alias="fullyLabeledReplicas"
    )

    observed_generation: int | None = Field(
        default_factory=lambda: None, alias="observedGeneration"
    )

    ready_replicas: int | None = Field(
        default_factory=lambda: None, alias="readyReplicas"
    )

    replicas: int | None = Field(default_factory=lambda: None)

    terminating_replicas: int | None = Field(
        default_factory=lambda: None, alias="terminatingReplicas"
    )
