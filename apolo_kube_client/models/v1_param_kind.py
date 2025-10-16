from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1ParamKind",)


class V1ParamKind(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")
