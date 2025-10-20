from pydantic import AliasChoices, BaseModel, Field
from datetime import datetime

__all__ = ("V1APIServiceCondition",)


class V1APIServiceCondition(BaseModel):
    last_transition_time: datetime | None = Field(
        default=None,
        serialization_alias="lastTransitionTime",
        validation_alias=AliasChoices("last_transition_time", "lastTransitionTime"),
    )

    message: str | None = None

    reason: str | None = None

    status: str | None = None

    type: str | None = None
