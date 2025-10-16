from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ("V1alpha1StorageVersionCondition",)


class V1alpha1StorageVersionCondition(BaseModel):
    last_transition_time: datetime | None = Field(
        default_factory=lambda: None, alias="lastTransitionTime"
    )

    message: str | None = Field(default_factory=lambda: None, alias="message")

    observed_generation: int | None = Field(
        default_factory=lambda: None, alias="observedGeneration"
    )

    reason: str | None = Field(default_factory=lambda: None, alias="reason")

    status: str | None = Field(default_factory=lambda: None, alias="status")

    type: str | None = Field(default_factory=lambda: None, alias="type")
