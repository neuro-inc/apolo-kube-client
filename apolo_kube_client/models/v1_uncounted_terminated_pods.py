from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1UncountedTerminatedPods",)


class V1UncountedTerminatedPods(BaseModel):
    failed: list[str] = Field(default_factory=lambda: [])

    succeeded: list[str] = Field(default_factory=lambda: [])
