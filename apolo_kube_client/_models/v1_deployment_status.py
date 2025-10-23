from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_deployment_condition import V1DeploymentCondition
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DeploymentStatus",)


class V1DeploymentStatus(BaseModel):
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
        list[V1DeploymentCondition], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

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

    terminating_replicas: int | None = Field(
        default=None,
        serialization_alias="terminatingReplicas",
        validation_alias=AliasChoices("terminating_replicas", "terminatingReplicas"),
        exclude_if=_exclude_if,
    )

    unavailable_replicas: int | None = Field(
        default=None,
        serialization_alias="unavailableReplicas",
        validation_alias=AliasChoices("unavailable_replicas", "unavailableReplicas"),
        exclude_if=_exclude_if,
    )

    updated_replicas: int | None = Field(
        default=None,
        serialization_alias="updatedReplicas",
        validation_alias=AliasChoices("updated_replicas", "updatedReplicas"),
        exclude_if=_exclude_if,
    )
