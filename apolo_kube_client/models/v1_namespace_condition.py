from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ("V1NamespaceCondition",)


class V1NamespaceCondition(BaseModel):
    last_transition_time: datetime | None = Field(
        default_factory=lambda: None, alias="lastTransitionTime"
    )

    message: str | None = Field(default_factory=lambda: None)

    reason: str | None = Field(default_factory=lambda: None)

    status: str | None = Field(default_factory=lambda: None)

    type: str | None = Field(default_factory=lambda: None)
