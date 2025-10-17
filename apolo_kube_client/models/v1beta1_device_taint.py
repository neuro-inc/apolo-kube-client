from pydantic import AliasChoices, BaseModel, Field
from datetime import datetime

__all__ = ("V1beta1DeviceTaint",)


class V1beta1DeviceTaint(BaseModel):
    effect: str | None = None

    key: str | None = None

    time_added: datetime | None = Field(
        default=None,
        serialization_alias="timeAdded",
        validation_alias=AliasChoices("time_added", "timeAdded"),
    )

    value: str | None = None
