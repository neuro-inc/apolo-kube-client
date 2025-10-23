from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ForZone",)


class V1ForZone(BaseModel):
    name: str | None = Field(default=None, exclude_if=_exclude_if)
