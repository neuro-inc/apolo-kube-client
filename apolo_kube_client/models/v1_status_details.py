from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_status_cause import V1StatusCause

__all__ = ("V1StatusDetails",)


class V1StatusDetails(BaseModel):
    causes: list[V1StatusCause] = Field(default=[])

    group: str | None = Field(default=None)

    kind: str | None = Field(default=None)

    name: str | None = Field(default=None)

    retry_after_seconds: int | None = Field(
        default=None,
        serialization_alias="retryAfterSeconds",
        validation_alias=AliasChoices("retry_after_seconds", "retryAfterSeconds"),
    )

    uid: str | None = Field(default=None)
