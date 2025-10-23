from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ConfigMapKeySelector",)


class V1ConfigMapKeySelector(BaseModel):
    key: str | None = Field(default=None, exclude_if=_exclude_if)

    name: str | None = Field(default=None, exclude_if=_exclude_if)

    optional: bool | None = Field(default=None, exclude_if=_exclude_if)
