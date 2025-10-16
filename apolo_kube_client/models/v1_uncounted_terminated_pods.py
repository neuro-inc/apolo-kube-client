from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1UncountedTerminatedPods",)


class V1UncountedTerminatedPods(BaseModel):
    failed: list[str] | None = Field(None, alias="failed")

    succeeded: list[str] | None = Field(None, alias="succeeded")
