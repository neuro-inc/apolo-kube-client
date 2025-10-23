from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ComponentCondition",)


class V1ComponentCondition(BaseModel):
    error: str | None = Field(default=None, exclude_if=_exclude_if)

    message: str | None = Field(default=None, exclude_if=_exclude_if)

    status: str | None = Field(default=None, exclude_if=_exclude_if)

    type: str | None = Field(default=None, exclude_if=_exclude_if)
