from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1ServiceAccountSubject",)


class V1ServiceAccountSubject(BaseModel):
    name: str | None = Field(None, alias="name")

    namespace: str | None = Field(None, alias="namespace")
