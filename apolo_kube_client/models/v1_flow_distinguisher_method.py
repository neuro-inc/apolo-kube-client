from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1FlowDistinguisherMethod",)


class V1FlowDistinguisherMethod(BaseModel):
    type: str | None = Field(default_factory=lambda: None)
