from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_replication_controller_condition import V1ReplicationControllerCondition
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ReplicationControllerStatus",)


class V1ReplicationControllerStatus(BaseModel):
    available_replicas: int | None = Field(
        default=None,
        serialization_alias="availableReplicas",
        validation_alias=AliasChoices("available_replicas", "availableReplicas"),
        exclude_if=_exclude_if,
    )

    conditions: Annotated[
        list[V1ReplicationControllerCondition],
        BeforeValidator(_collection_if_none("[]")),
    ] = Field(default=[], exclude_if=_exclude_if)

    fully_labeled_replicas: int | None = Field(
        default=None,
        serialization_alias="fullyLabeledReplicas",
        validation_alias=AliasChoices("fully_labeled_replicas", "fullyLabeledReplicas"),
        exclude_if=_exclude_if,
    )

    observed_generation: int | None = Field(
        default=None,
        serialization_alias="observedGeneration",
        validation_alias=AliasChoices("observed_generation", "observedGeneration"),
        exclude_if=_exclude_if,
    )

    ready_replicas: int | None = Field(
        default=None,
        serialization_alias="readyReplicas",
        validation_alias=AliasChoices("ready_replicas", "readyReplicas"),
        exclude_if=_exclude_if,
    )

    replicas: int | None = Field(default=None, exclude_if=_exclude_if)
