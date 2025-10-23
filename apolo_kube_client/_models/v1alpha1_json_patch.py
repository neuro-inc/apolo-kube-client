from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1alpha1JSONPatch",)


class V1alpha1JSONPatch(BaseModel):
    expression: str | None = Field(default=None, exclude_if=_exclude_if)
