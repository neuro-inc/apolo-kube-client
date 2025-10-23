from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1NonResourceAttributes",)


class V1NonResourceAttributes(BaseModel):
    path: str | None = Field(default=None, exclude_if=_exclude_if)

    verb: str | None = Field(default=None, exclude_if=_exclude_if)
