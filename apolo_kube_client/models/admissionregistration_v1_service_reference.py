from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("AdmissionregistrationV1ServiceReference",)


class AdmissionregistrationV1ServiceReference(BaseModel):
    name: str | None = Field(default_factory=lambda: None, alias="name")

    namespace: str | None = Field(default_factory=lambda: None, alias="namespace")

    path: str | None = Field(default_factory=lambda: None, alias="path")

    port: int | None = Field(default_factory=lambda: None, alias="port")
