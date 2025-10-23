from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if
from datetime import datetime

__all__ = ("V1VolumeError",)


class V1VolumeError(BaseModel):
    error_code: int | None = Field(
        default=None,
        serialization_alias="errorCode",
        validation_alias=AliasChoices("error_code", "errorCode"),
        exclude_if=_exclude_if,
    )

    message: str | None = Field(default=None, exclude_if=_exclude_if)

    time: datetime | None = Field(default=None, exclude_if=_exclude_if)
