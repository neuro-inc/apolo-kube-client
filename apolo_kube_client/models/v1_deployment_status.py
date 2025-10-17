from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_deployment_condition import V1DeploymentCondition

__all__ = ("V1DeploymentStatus",)


class V1DeploymentStatus(BaseModel):
    available_replicas: int | None = Field(
        default_factory=lambda: None, alias="availableReplicas"
    )

    collision_count: int | None = Field(
        default_factory=lambda: None, alias="collisionCount"
    )

    conditions: list[V1DeploymentCondition] = Field(default_factory=lambda: [])

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

    unavailable_replicas: int | None = Field(
        default_factory=lambda: None, alias="unavailableReplicas"
    )

    updated_replicas: int | None = Field(
        default_factory=lambda: None, alias="updatedReplicas"
    )
