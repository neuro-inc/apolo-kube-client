from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1PodIP",)


class V1PodIP(BaseModel):
    ip: str | None = Field(default_factory=lambda: None, alias="ip")
