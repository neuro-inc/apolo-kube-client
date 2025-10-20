from pydantic import AliasChoices, BaseModel, Field
from .v1_daemon_set_condition import V1DaemonSetCondition

__all__ = ("V1DaemonSetStatus",)


class V1DaemonSetStatus(BaseModel):
    collision_count: int | None = Field(
        default=None,
        serialization_alias="collisionCount",
        validation_alias=AliasChoices("collision_count", "collisionCount"),
    )

    conditions: list[V1DaemonSetCondition] = []

    current_number_scheduled: int | None = Field(
        default=None,
        serialization_alias="currentNumberScheduled",
        validation_alias=AliasChoices(
            "current_number_scheduled", "currentNumberScheduled"
        ),
    )

    desired_number_scheduled: int | None = Field(
        default=None,
        serialization_alias="desiredNumberScheduled",
        validation_alias=AliasChoices(
            "desired_number_scheduled", "desiredNumberScheduled"
        ),
    )

    number_available: int | None = Field(
        default=None,
        serialization_alias="numberAvailable",
        validation_alias=AliasChoices("number_available", "numberAvailable"),
    )

    number_misscheduled: int | None = Field(
        default=None,
        serialization_alias="numberMisscheduled",
        validation_alias=AliasChoices("number_misscheduled", "numberMisscheduled"),
    )

    number_ready: int | None = Field(
        default=None,
        serialization_alias="numberReady",
        validation_alias=AliasChoices("number_ready", "numberReady"),
    )

    number_unavailable: int | None = Field(
        default=None,
        serialization_alias="numberUnavailable",
        validation_alias=AliasChoices("number_unavailable", "numberUnavailable"),
    )

    observed_generation: int | None = Field(
        default=None,
        serialization_alias="observedGeneration",
        validation_alias=AliasChoices("observed_generation", "observedGeneration"),
    )

    updated_number_scheduled: int | None = Field(
        default=None,
        serialization_alias="updatedNumberScheduled",
        validation_alias=AliasChoices(
            "updated_number_scheduled", "updatedNumberScheduled"
        ),
    )
