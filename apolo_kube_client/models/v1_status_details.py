from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_status_cause import V1StatusCause

__all__ = ("V1StatusDetails",)


class V1StatusDetails(BaseModel):
    causes: list[V1StatusCause] = Field(default_factory=lambda: [])

    group: str | None = Field(default_factory=lambda: None)

    kind: str | None = Field(default_factory=lambda: None)

    name: str | None = Field(default_factory=lambda: None)

    retry_after_seconds: int | None = Field(
        default_factory=lambda: None, alias="retryAfterSeconds"
    )

    uid: str | None = Field(default_factory=lambda: None)
