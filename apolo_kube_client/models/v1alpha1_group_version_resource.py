from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1alpha1GroupVersionResource",)


class V1alpha1GroupVersionResource(BaseModel):
    group: str | None = Field(default=None)

    resource: str | None = Field(default=None)

    version: str | None = Field(default=None)
