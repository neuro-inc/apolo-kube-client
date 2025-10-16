from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_daemon_set_condition import V1DaemonSetCondition

__all__ = ("V1DaemonSetStatus",)


class V1DaemonSetStatus(BaseModel):
    collision_count: int | None = Field(
        default_factory=lambda: None, alias="collisionCount"
    )

    conditions: list[V1DaemonSetCondition] = Field(
        default_factory=lambda: [], alias="conditions"
    )

    current_number_scheduled: int | None = Field(
        default_factory=lambda: None, alias="currentNumberScheduled"
    )

    desired_number_scheduled: int | None = Field(
        default_factory=lambda: None, alias="desiredNumberScheduled"
    )

    number_available: int | None = Field(
        default_factory=lambda: None, alias="numberAvailable"
    )

    number_misscheduled: int | None = Field(
        default_factory=lambda: None, alias="numberMisscheduled"
    )

    number_ready: int | None = Field(default_factory=lambda: None, alias="numberReady")

    number_unavailable: int | None = Field(
        default_factory=lambda: None, alias="numberUnavailable"
    )

    observed_generation: int | None = Field(
        default_factory=lambda: None, alias="observedGeneration"
    )

    updated_number_scheduled: int | None = Field(
        default_factory=lambda: None, alias="updatedNumberScheduled"
    )
