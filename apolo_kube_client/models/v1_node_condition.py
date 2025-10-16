from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ("V1NodeCondition",)


class V1NodeCondition(BaseModel):
    last_heartbeat_time: datetime | None = Field(
        default_factory=lambda: None, alias="lastHeartbeatTime"
    )

    last_transition_time: datetime | None = Field(
        default_factory=lambda: None, alias="lastTransitionTime"
    )

    message: str | None = Field(default_factory=lambda: None, alias="message")

    reason: str | None = Field(default_factory=lambda: None, alias="reason")

    status: str | None = Field(default_factory=lambda: None, alias="status")

    type: str | None = Field(default_factory=lambda: None, alias="type")
