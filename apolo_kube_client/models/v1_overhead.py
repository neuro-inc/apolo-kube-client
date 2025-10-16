from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1Overhead",)


class V1Overhead(BaseModel):
    pod_fixed: dict[str, str] = Field(default_factory=lambda: {}, alias="podFixed")
