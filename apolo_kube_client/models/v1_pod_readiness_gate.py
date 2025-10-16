from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1PodReadinessGate",)


class V1PodReadinessGate(BaseModel):
    condition_type: str | None = Field(
        default_factory=lambda: None, alias="conditionType"
    )
