from pydantic import AliasChoices, BaseModel, Field
from datetime import datetime

__all__ = ("V1PersistentVolumeStatus",)


class V1PersistentVolumeStatus(BaseModel):
    last_phase_transition_time: datetime | None = Field(
        default=None,
        serialization_alias="lastPhaseTransitionTime",
        validation_alias=AliasChoices(
            "last_phase_transition_time", "lastPhaseTransitionTime"
        ),
    )

    message: str | None = None

    phase: str | None = None

    reason: str | None = None
