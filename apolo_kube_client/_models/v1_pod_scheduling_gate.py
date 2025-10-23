from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1PodSchedulingGate",)


class V1PodSchedulingGate(BaseModel):
    name: str | None = Field(default=None, exclude_if=_exclude_if)
