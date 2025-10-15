from datetime import datetime

from pydantic import BaseModel, Field


class V1PersistentVolumeStatus(BaseModel):
    last_phase_transition_time: datetime | None = Field(
        None, alias="lastPhaseTransitionTime"
    )

    message: str | None = Field(None, alias="message")

    phase: str | None = Field(None, alias="phase")

    reason: str | None = Field(None, alias="reason")
