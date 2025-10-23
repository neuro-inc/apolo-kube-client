from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1KeyToPath",)


class V1KeyToPath(BaseModel):
    key: str | None = Field(default=None, exclude_if=_exclude_if)

    mode: int | None = Field(default=None, exclude_if=_exclude_if)

    path: str | None = Field(default=None, exclude_if=_exclude_if)
