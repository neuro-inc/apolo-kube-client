from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ExternalDocumentation",)


class V1ExternalDocumentation(BaseModel):
    description: str | None = Field(default_factory=lambda: None)

    url: str | None = Field(default_factory=lambda: None)
