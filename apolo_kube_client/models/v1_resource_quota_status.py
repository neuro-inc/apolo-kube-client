from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ResourceQuotaStatus",)


class V1ResourceQuotaStatus(BaseModel):
    hard: dict[str, str] = Field(default_factory=lambda: {}, alias="hard")

    used: dict[str, str] = Field(default_factory=lambda: {}, alias="used")
