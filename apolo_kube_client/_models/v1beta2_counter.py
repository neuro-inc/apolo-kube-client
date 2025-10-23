from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1beta2Counter",)


class V1beta2Counter(BaseModel):
    value: str | None = Field(default=None, exclude_if=_exclude_if)
