from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1SELinuxOptions",)


class V1SELinuxOptions(BaseModel):
    level: str | None = Field(default=None, exclude_if=_exclude_if)

    role: str | None = Field(default=None, exclude_if=_exclude_if)

    type: str | None = Field(default=None, exclude_if=_exclude_if)

    user: str | None = Field(default=None, exclude_if=_exclude_if)
