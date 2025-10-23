from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1EventSource",)


class V1EventSource(BaseModel):
    component: str | None = Field(default=None, exclude_if=_exclude_if)

    host: str | None = Field(default=None, exclude_if=_exclude_if)
