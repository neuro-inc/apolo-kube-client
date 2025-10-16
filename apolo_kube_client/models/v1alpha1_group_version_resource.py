from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1alpha1GroupVersionResource",)


class V1alpha1GroupVersionResource(BaseModel):
    group: str | None = Field(None, alias="group")

    resource: str | None = Field(None, alias="resource")

    version: str | None = Field(None, alias="version")
