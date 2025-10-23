from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1IngressPortStatus",)


class V1IngressPortStatus(BaseModel):
    error: str | None = Field(default=None, exclude_if=_exclude_if)

    port: int | None = Field(default=None, exclude_if=_exclude_if)

    protocol: str | None = Field(default=None, exclude_if=_exclude_if)
