from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ExecAction",)


class V1ExecAction(BaseModel):
    command: list[str] = Field(default_factory=lambda: [], alias="command")
