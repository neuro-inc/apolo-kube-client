from pydantic import BaseModel, Field

from .v1_daemon_set_condition import V1DaemonSetCondition


class V1DaemonSetStatus(BaseModel):
    collision_count: int | None = Field(None, alias="collisionCount")

    conditions: list[V1DaemonSetCondition] | None = Field(None, alias="conditions")

    current_number_scheduled: int | None = Field(None, alias="currentNumberScheduled")

    desired_number_scheduled: int | None = Field(None, alias="desiredNumberScheduled")

    number_available: int | None = Field(None, alias="numberAvailable")

    number_misscheduled: int | None = Field(None, alias="numberMisscheduled")

    number_ready: int | None = Field(None, alias="numberReady")

    number_unavailable: int | None = Field(None, alias="numberUnavailable")

    observed_generation: int | None = Field(None, alias="observedGeneration")

    updated_number_scheduled: int | None = Field(None, alias="updatedNumberScheduled")
