from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_replica_set_condition import V1ReplicaSetCondition

__all__ = ("V1ReplicaSetStatus",)


class V1ReplicaSetStatus(BaseModel):
    available_replicas: int | None = Field(None, alias="availableReplicas")

    conditions: list[V1ReplicaSetCondition] | None = Field(None, alias="conditions")

    fully_labeled_replicas: int | None = Field(None, alias="fullyLabeledReplicas")

    observed_generation: int | None = Field(None, alias="observedGeneration")

    ready_replicas: int | None = Field(None, alias="readyReplicas")

    replicas: int | None = Field(None, alias="replicas")
