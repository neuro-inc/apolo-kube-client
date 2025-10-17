from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ServiceAccountSubject",)


class V1ServiceAccountSubject(BaseModel):
    name: str | None = Field(default=None)

    namespace: str | None = Field(default=None)
