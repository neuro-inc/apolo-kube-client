from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1PodIP",)


class V1PodIP(BaseModel):
    ip: str | None = Field(default=None, exclude_if=_exclude_if)
