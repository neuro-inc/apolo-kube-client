from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if
from datetime import datetime

__all__ = ("V1PersistentVolumeStatus",)


class V1PersistentVolumeStatus(BaseModel):
    last_phase_transition_time: datetime | None = Field(
        default=None,
        serialization_alias="lastPhaseTransitionTime",
        validation_alias=AliasChoices(
            "last_phase_transition_time", "lastPhaseTransitionTime"
        ),
        exclude_if=_exclude_if,
    )

    message: str | None = Field(default=None, exclude_if=_exclude_if)

    phase: str | None = Field(default=None, exclude_if=_exclude_if)

    reason: str | None = Field(default=None, exclude_if=_exclude_if)
