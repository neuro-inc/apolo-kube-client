from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1SecretReference",)


class V1SecretReference(BaseModel):
    name: str | None = Field(None, alias="name")

    namespace: str | None = Field(None, alias="namespace")
