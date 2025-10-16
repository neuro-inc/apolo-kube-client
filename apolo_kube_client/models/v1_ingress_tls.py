from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1IngressTLS",)


class V1IngressTLS(BaseModel):
    hosts: list[str] = Field(default_factory=lambda: [], alias="hosts")

    secret_name: str | None = Field(default_factory=lambda: None, alias="secretName")
