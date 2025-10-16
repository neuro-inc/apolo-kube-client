from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ScaleStatus",)


class V1ScaleStatus(BaseModel):
    replicas: int | None = Field(default_factory=lambda: None, alias="replicas")

    selector: str | None = Field(default_factory=lambda: None, alias="selector")
