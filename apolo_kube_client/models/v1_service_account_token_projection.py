from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1ServiceAccountTokenProjection",)


class V1ServiceAccountTokenProjection(BaseModel):
    audience: str | None = Field(None, alias="audience")

    expiration_seconds: int | None = Field(None, alias="expirationSeconds")

    path: str | None = Field(None, alias="path")
