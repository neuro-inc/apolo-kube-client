from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_stateful_set_condition import V1StatefulSetCondition

__all__ = ("V1StatefulSetStatus",)


class V1StatefulSetStatus(BaseModel):
    available_replicas: int | None = Field(
        default_factory=lambda: None, alias="availableReplicas"
    )

    collision_count: int | None = Field(
        default_factory=lambda: None, alias="collisionCount"
    )

    conditions: list[V1StatefulSetCondition] = Field(default_factory=lambda: [])

    current_replicas: int | None = Field(
        default_factory=lambda: None, alias="currentReplicas"
    )

    current_revision: str | None = Field(
        default_factory=lambda: None, alias="currentRevision"
    )

    observed_generation: int | None = Field(
        default_factory=lambda: None, alias="observedGeneration"
    )

    ready_replicas: int | None = Field(
        default_factory=lambda: None, alias="readyReplicas"
    )

    replicas: int | None = Field(default_factory=lambda: None)

    update_revision: str | None = Field(
        default_factory=lambda: None, alias="updateRevision"
    )

    updated_replicas: int | None = Field(
        default_factory=lambda: None, alias="updatedReplicas"
    )
