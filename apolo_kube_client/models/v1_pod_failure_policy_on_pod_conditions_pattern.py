from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1PodFailurePolicyOnPodConditionsPattern",)


class V1PodFailurePolicyOnPodConditionsPattern(BaseModel):
    status: str | None = Field(default_factory=lambda: None, alias="status")

    type: str | None = Field(default_factory=lambda: None, alias="type")
