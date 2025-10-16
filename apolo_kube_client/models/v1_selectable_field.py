from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1SelectableField",)


class V1SelectableField(BaseModel):
    json_path: str | None = Field(default_factory=lambda: None, alias="jsonPath")
