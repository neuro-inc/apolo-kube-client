from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ("V1NamespaceCondition",)


class V1NamespaceCondition(BaseModel):
    last_transition_time: datetime | None = Field(
        default_factory=lambda: None, alias="lastTransitionTime"
    )

    message: str | None = Field(default_factory=lambda: None, alias="message")

    reason: str | None = Field(default_factory=lambda: None, alias="reason")

    status: str | None = Field(default_factory=lambda: None, alias="status")

    type: str | None = Field(default_factory=lambda: None, alias="type")
