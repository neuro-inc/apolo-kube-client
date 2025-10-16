from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_replication_controller_condition import V1ReplicationControllerCondition

__all__ = ("V1ReplicationControllerStatus",)


class V1ReplicationControllerStatus(BaseModel):
    available_replicas: int | None = Field(
        default_factory=lambda: None, alias="availableReplicas"
    )

    conditions: list[V1ReplicationControllerCondition] = Field(
        default_factory=lambda: [], alias="conditions"
    )

    fully_labeled_replicas: int | None = Field(
        default_factory=lambda: None, alias="fullyLabeledReplicas"
    )

    observed_generation: int | None = Field(
        default_factory=lambda: None, alias="observedGeneration"
    )

    ready_replicas: int | None = Field(
        default_factory=lambda: None, alias="readyReplicas"
    )

    replicas: int | None = Field(default_factory=lambda: None, alias="replicas")
