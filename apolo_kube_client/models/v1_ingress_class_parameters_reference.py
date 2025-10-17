from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1IngressClassParametersReference",)


class V1IngressClassParametersReference(BaseModel):
    api_group: str | None = Field(default_factory=lambda: None, alias="apiGroup")

    kind: str | None = Field(default_factory=lambda: None)

    name: str | None = Field(default_factory=lambda: None)

    namespace: str | None = Field(default_factory=lambda: None)

    scope: str | None = Field(default_factory=lambda: None)
