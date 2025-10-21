from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_replication_controller_condition import V1ReplicationControllerCondition
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ReplicationControllerStatus",)


class V1ReplicationControllerStatus(BaseModel):
    available_replicas: int | None = Field(
        default=None,
        serialization_alias="availableReplicas",
        validation_alias=AliasChoices("available_replicas", "availableReplicas"),
    )

    conditions: Annotated[
        list[V1ReplicationControllerCondition],
        BeforeValidator(_collection_if_none("[]")),
    ] = []

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
