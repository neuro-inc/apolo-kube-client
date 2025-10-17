from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_deployment_condition import V1DeploymentCondition

__all__ = ("V1DeploymentStatus",)


class V1DeploymentStatus(BaseModel):
    available_replicas: int | None = Field(
        default=None,
        serialization_alias="availableReplicas",
        validation_alias=AliasChoices("available_replicas", "availableReplicas"),
    )

    collision_count: int | None = Field(
        default=None,
        serialization_alias="collisionCount",
        validation_alias=AliasChoices("collision_count", "collisionCount"),
    )

    conditions: list[V1DeploymentCondition] = Field(default=[])

    observed_generation: int | None = Field(
        default=None,
        serialization_alias="observedGeneration",
        validation_alias=AliasChoices("observed_generation", "observedGeneration"),
    )

    ready_replicas: int | None = Field(
        default=None,
        serialization_alias="readyReplicas",
        validation_alias=AliasChoices("ready_replicas", "readyReplicas"),
    )

    replicas: int | None = Field(default=None)

    terminating_replicas: int | None = Field(
        default=None,
        serialization_alias="terminatingReplicas",
        validation_alias=AliasChoices("terminating_replicas", "terminatingReplicas"),
    )

    unavailable_replicas: int | None = Field(
        default=None,
        serialization_alias="unavailableReplicas",
        validation_alias=AliasChoices("unavailable_replicas", "unavailableReplicas"),
    )

    updated_replicas: int | None = Field(
        default=None,
        serialization_alias="updatedReplicas",
        validation_alias=AliasChoices("updated_replicas", "updatedReplicas"),
    )
