from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1GroupSubject",)


class V1GroupSubject(BaseModel):
    name: str | None = Field(default=None, exclude_if=_exclude_if)
