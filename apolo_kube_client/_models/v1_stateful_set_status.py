from pydantic import AliasChoices, BaseModel, Field
from .v1_stateful_set_condition import V1StatefulSetCondition

__all__ = ("V1StatefulSetStatus",)


class V1StatefulSetStatus(BaseModel):
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

    conditions: list[V1StatefulSetCondition] = []

    current_replicas: int | None = Field(
        default=None,
        serialization_alias="currentReplicas",
        validation_alias=AliasChoices("current_replicas", "currentReplicas"),
    )

    current_revision: str | None = Field(
        default=None,
        serialization_alias="currentRevision",
        validation_alias=AliasChoices("current_revision", "currentRevision"),
    )

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

    replicas: int | None = None

    update_revision: str | None = Field(
        default=None,
        serialization_alias="updateRevision",
        validation_alias=AliasChoices("update_revision", "updateRevision"),
    )

    updated_replicas: int | None = Field(
        default=None,
        serialization_alias="updatedReplicas",
        validation_alias=AliasChoices("updated_replicas", "updatedReplicas"),
    )
