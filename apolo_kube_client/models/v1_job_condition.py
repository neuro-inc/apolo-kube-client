from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from datetime import datetime

__all__ = ("V1JobCondition",)


class V1JobCondition(BaseModel):
    last_probe_time: datetime | None = Field(
        default=None,
        serialization_alias="lastProbeTime",
        validation_alias=AliasChoices("last_probe_time", "lastProbeTime"),
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
