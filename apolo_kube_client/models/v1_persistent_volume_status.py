from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ("V1PersistentVolumeStatus",)


class V1PersistentVolumeStatus(BaseModel):
    last_phase_transition_time: datetime | None = Field(
        default_factory=lambda: None, alias="lastPhaseTransitionTime"
    )

    message: str | None = Field(default_factory=lambda: None, alias="message")

    phase: str | None = Field(default_factory=lambda: None, alias="phase")

    reason: str | None = Field(default_factory=lambda: None, alias="reason")
