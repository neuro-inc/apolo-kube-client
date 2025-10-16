from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ObjectFieldSelector",)


class V1ObjectFieldSelector(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    field_path: str | None = Field(default_factory=lambda: None, alias="fieldPath")
