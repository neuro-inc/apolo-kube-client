from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1alpha1ApplyConfiguration",)


class V1alpha1ApplyConfiguration(BaseModel):
    expression: str | None = Field(default=None, exclude_if=_exclude_if)
