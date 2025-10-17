from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from datetime import datetime

__all__ = ("V1NodeCondition",)


class V1NodeCondition(BaseModel):
    last_heartbeat_time: datetime | None = Field(
        default=None,
        serialization_alias="lastHeartbeatTime",
        validation_alias=AliasChoices("last_heartbeat_time", "lastHeartbeatTime"),
    )

    last_transition_time: datetime | None = Field(
        default=None,
        serialization_alias="lastTransitionTime",
        validation_alias=AliasChoices("last_transition_time", "lastTransitionTime"),
    )

    message: str | None = Field(default=None)

    reason: str | None = Field(default=None)

    status: str | None = Field(default=None)

    type: str | None = Field(default=None)
