from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_daemon_set_condition import V1DaemonSetCondition
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DaemonSetStatus",)


class V1DaemonSetStatus(BaseModel):
    collision_count: int | None = Field(
        default=None,
        serialization_alias="collisionCount",
        validation_alias=AliasChoices("collision_count", "collisionCount"),
        exclude_if=_exclude_if,
    )

    conditions: Annotated[
        list[V1DaemonSetCondition], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    current_number_scheduled: int | None = Field(
        default=None,
        serialization_alias="currentNumberScheduled",
        validation_alias=AliasChoices(
            "current_number_scheduled", "currentNumberScheduled"
        ),
        exclude_if=_exclude_if,
    )

    desired_number_scheduled: int | None = Field(
        default=None,
        serialization_alias="desiredNumberScheduled",
        validation_alias=AliasChoices(
            "desired_number_scheduled", "desiredNumberScheduled"
        ),
        exclude_if=_exclude_if,
    )

    number_available: int | None = Field(
        default=None,
        serialization_alias="numberAvailable",
        validation_alias=AliasChoices("number_available", "numberAvailable"),
        exclude_if=_exclude_if,
    )

    number_misscheduled: int | None = Field(
        default=None,
        serialization_alias="numberMisscheduled",
        validation_alias=AliasChoices("number_misscheduled", "numberMisscheduled"),
        exclude_if=_exclude_if,
    )

    number_ready: int | None = Field(
        default=None,
        serialization_alias="numberReady",
        validation_alias=AliasChoices("number_ready", "numberReady"),
        exclude_if=_exclude_if,
    )

    number_unavailable: int | None = Field(
        default=None,
        serialization_alias="numberUnavailable",
        validation_alias=AliasChoices("number_unavailable", "numberUnavailable"),
        exclude_if=_exclude_if,
    )

    observed_generation: int | None = Field(
        default=None,
        serialization_alias="observedGeneration",
        validation_alias=AliasChoices("observed_generation", "observedGeneration"),
        exclude_if=_exclude_if,
    )

    updated_number_scheduled: int | None = Field(
        default=None,
        serialization_alias="updatedNumberScheduled",
        validation_alias=AliasChoices(
            "updated_number_scheduled", "updatedNumberScheduled"
        ),
        exclude_if=_exclude_if,
    )
