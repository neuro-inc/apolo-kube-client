from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1IngressTLS",)


class V1IngressTLS(BaseModel):
    hosts: list[str] | None = Field(None, alias="hosts")

    secret_name: str | None = Field(None, alias="secretName")
