from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("AdmissionregistrationV1ServiceReference",)


class AdmissionregistrationV1ServiceReference(BaseModel):
    name: str | None = Field(default=None)

    namespace: str | None = Field(default=None)

    path: str | None = Field(default=None)

    port: int | None = Field(default=None)
