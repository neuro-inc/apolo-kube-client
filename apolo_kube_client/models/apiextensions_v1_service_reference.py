from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("ApiextensionsV1ServiceReference",)


class ApiextensionsV1ServiceReference(BaseModel):
    name: str | None = Field(default_factory=lambda: None)

    namespace: str | None = Field(default_factory=lambda: None)

    path: str | None = Field(default_factory=lambda: None)

    port: int | None = Field(default_factory=lambda: None)
