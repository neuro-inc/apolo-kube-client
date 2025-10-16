from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ClientIPConfig",)


class V1ClientIPConfig(BaseModel):
    timeout_seconds: int | None = Field(
        default_factory=lambda: None, alias="timeoutSeconds"
    )
