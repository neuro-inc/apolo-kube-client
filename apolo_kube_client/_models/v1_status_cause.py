from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1StatusCause",)


class V1StatusCause(BaseModel):
    field: str | None = Field(default=None, exclude_if=_exclude_if)

    message: str | None = Field(default=None, exclude_if=_exclude_if)

    reason: str | None = Field(default=None, exclude_if=_exclude_if)
