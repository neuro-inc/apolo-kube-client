from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_replica_set_condition import V1ReplicaSetCondition
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ReplicaSetStatus",)


class V1ReplicaSetStatus(BaseModel):
    available_replicas: int | None = Field(
        default=None,
        serialization_alias="availableReplicas",
        validation_alias=AliasChoices("available_replicas", "availableReplicas"),
    )

    conditions: Annotated[
        list[V1ReplicaSetCondition], BeforeValidator(_collection_if_none("[]"))
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

    terminating_replicas: int | None = Field(
        default=None,
        serialization_alias="terminatingReplicas",
        validation_alias=AliasChoices("terminating_replicas", "terminatingReplicas"),
    )
