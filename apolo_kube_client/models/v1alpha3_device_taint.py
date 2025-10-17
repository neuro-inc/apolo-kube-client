from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from datetime import datetime

__all__ = ("V1alpha3DeviceTaint",)


class V1alpha3DeviceTaint(BaseModel):
    effect: str | None = Field(default=None)

    key: str | None = Field(default=None)

    time_added: datetime | None = Field(
        default=None,
        serialization_alias="timeAdded",
        validation_alias=AliasChoices("time_added", "timeAdded"),
    )

    value: str | None = Field(default=None)
