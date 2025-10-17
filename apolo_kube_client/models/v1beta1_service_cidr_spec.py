from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1beta1ServiceCIDRSpec",)


class V1beta1ServiceCIDRSpec(BaseModel):
    cidrs: list[str] = Field(default_factory=lambda: [])
