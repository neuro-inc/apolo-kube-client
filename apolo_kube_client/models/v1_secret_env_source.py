from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1SecretEnvSource",)


class V1SecretEnvSource(BaseModel):
    name: str | None = Field(None, alias="name")

    optional: bool | None = Field(None, alias="optional")
