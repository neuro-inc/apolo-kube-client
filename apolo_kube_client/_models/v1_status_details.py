from pydantic import AliasChoices, BaseModel, Field
from .v1_status_cause import V1StatusCause

__all__ = ("V1StatusDetails",)


class V1StatusDetails(BaseModel):
    causes: list[V1StatusCause] = []

    group: str | None = None

    kind: str | None = None

    name: str | None = None

    retry_after_seconds: int | None = Field(
        default=None,
        serialization_alias="retryAfterSeconds",
        validation_alias=AliasChoices("retry_after_seconds", "retryAfterSeconds"),
    )

    uid: str | None = None
