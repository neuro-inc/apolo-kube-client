from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1beta1JSONPatch",)


class V1beta1JSONPatch(BaseModel):
    expression: str | None = Field(default=None, exclude_if=_exclude_if)
