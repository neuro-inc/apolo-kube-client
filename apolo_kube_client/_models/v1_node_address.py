from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1NodeAddress",)


class V1NodeAddress(BaseModel):
    address: str | None = Field(default=None, exclude_if=_exclude_if)

    type: str | None = Field(default=None, exclude_if=_exclude_if)
