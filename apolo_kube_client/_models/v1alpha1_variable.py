from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1alpha1Variable",)


class V1alpha1Variable(BaseModel):
    expression: str | None = Field(default=None, exclude_if=_exclude_if)

    name: str | None = Field(default=None, exclude_if=_exclude_if)
