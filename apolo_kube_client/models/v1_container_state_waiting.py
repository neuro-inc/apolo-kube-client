from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ContainerStateWaiting",)


class V1ContainerStateWaiting(BaseModel):
    message: str | None = Field(default=None)

    reason: str | None = Field(default=None)
