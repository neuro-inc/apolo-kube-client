from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ServiceAccountTokenProjection",)


class V1ServiceAccountTokenProjection(BaseModel):
    audience: str | None = Field(default_factory=lambda: None, alias="audience")

    expiration_seconds: int | None = Field(
        default_factory=lambda: None, alias="expirationSeconds"
    )

    path: str | None = Field(default_factory=lambda: None, alias="path")
