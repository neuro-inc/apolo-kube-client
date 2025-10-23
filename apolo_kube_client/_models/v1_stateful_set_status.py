from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_stateful_set_condition import V1StatefulSetCondition
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1StatefulSetStatus",)


class V1StatefulSetStatus(BaseModel):
    available_replicas: int | None = Field(
        default=None,
        serialization_alias="availableReplicas",
        validation_alias=AliasChoices("available_replicas", "availableReplicas"),
        exclude_if=_exclude_if,
    )

    collision_count: int | None = Field(
        default=None,
        serialization_alias="collisionCount",
        validation_alias=AliasChoices("collision_count", "collisionCount"),
        exclude_if=_exclude_if,
    )

    conditions: Annotated[
        list[V1StatefulSetCondition], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    current_replicas: int | None = Field(
        default=None,
        serialization_alias="currentReplicas",
        validation_alias=AliasChoices("current_replicas", "currentReplicas"),
        exclude_if=_exclude_if,
    )

    current_revision: str | None = Field(
        default=None,
        serialization_alias="currentRevision",
        validation_alias=AliasChoices("current_revision", "currentRevision"),
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

    update_revision: str | None = Field(
        default=None,
        serialization_alias="updateRevision",
        validation_alias=AliasChoices("update_revision", "updateRevision"),
        exclude_if=_exclude_if,
    )

    updated_replicas: int | None = Field(
        default=None,
        serialization_alias="updatedReplicas",
        validation_alias=AliasChoices("updated_replicas", "updatedReplicas"),
        exclude_if=_exclude_if,
    )
