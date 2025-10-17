from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from datetime import datetime

__all__ = ("V1VolumeError",)


class V1VolumeError(BaseModel):
    error_code: int | None = Field(
        default=None,
        serialization_alias="errorCode",
        validation_alias=AliasChoices("error_code", "errorCode"),
    )

    message: str | None = Field(default=None)

    time: datetime | None = Field(default=None)
