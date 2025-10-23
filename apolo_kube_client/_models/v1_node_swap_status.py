from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1NodeSwapStatus",)


class V1NodeSwapStatus(BaseModel):
    capacity: int | None = Field(default=None, exclude_if=_exclude_if)
