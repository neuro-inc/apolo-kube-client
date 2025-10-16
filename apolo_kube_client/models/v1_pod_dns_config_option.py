from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1PodDNSConfigOption",)


class V1PodDNSConfigOption(BaseModel):
    name: str | None = Field(default_factory=lambda: None, alias="name")

    value: str | None = Field(default_factory=lambda: None, alias="value")
