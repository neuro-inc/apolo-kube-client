from pydantic import AliasChoices, BaseModel, Field
from .v1_replication_controller_condition import V1ReplicationControllerCondition

__all__ = ("V1ReplicationControllerStatus",)


class V1ReplicationControllerStatus(BaseModel):
    available_replicas: int | None = Field(
        default=None,
        serialization_alias="availableReplicas",
        validation_alias=AliasChoices("available_replicas", "availableReplicas"),
    )

    conditions: list[V1ReplicationControllerCondition] = []

    fully_labeled_replicas: int | None = Field(
        default=None,
        serialization_alias="fullyLabeledReplicas",
        validation_alias=AliasChoices("fully_labeled_replicas", "fullyLabeledReplicas"),
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
