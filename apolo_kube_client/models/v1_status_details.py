from pydantic import BaseModel, Field

from .v1_status_cause import V1StatusCause


class V1StatusDetails(BaseModel):
    causes: list[V1StatusCause] | None = Field(None, alias="causes")

    group: str | None = Field(None, alias="group")

    kind: str | None = Field(None, alias="kind")

    name: str | None = Field(None, alias="name")

    retry_after_seconds: int | None = Field(None, alias="retryAfterSeconds")

    uid: str | None = Field(None, alias="uid")
