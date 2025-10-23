from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if
from datetime import datetime

__all__ = ("V1Taint",)


class V1Taint(BaseModel):
    effect: str | None = Field(default=None, exclude_if=_exclude_if)

    key: str | None = Field(default=None, exclude_if=_exclude_if)

    time_added: datetime | None = Field(
        default=None,
        serialization_alias="timeAdded",
        validation_alias=AliasChoices("time_added", "timeAdded"),
        exclude_if=_exclude_if,
    )

    value: str | None = Field(default=None, exclude_if=_exclude_if)
