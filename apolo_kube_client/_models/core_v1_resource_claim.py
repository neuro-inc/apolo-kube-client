from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("CoreV1ResourceClaim",)


class CoreV1ResourceClaim(BaseModel):
    name: str | None = Field(default=None, exclude_if=_exclude_if)

    request: str | None = Field(default=None, exclude_if=_exclude_if)
