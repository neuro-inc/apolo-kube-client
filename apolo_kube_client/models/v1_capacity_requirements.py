from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1CapacityRequirements",)


class V1CapacityRequirements(BaseModel):
    requests: dict[str, str] = Field(default={})
