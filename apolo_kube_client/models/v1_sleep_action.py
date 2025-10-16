from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1SleepAction",)


class V1SleepAction(BaseModel):
    seconds: int | None = Field(default_factory=lambda: None, alias="seconds")
