from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1Sysctl",)


class V1Sysctl(BaseModel):
    name: str | None = Field(default=None, exclude_if=_exclude_if)

    value: str | None = Field(default=None, exclude_if=_exclude_if)
