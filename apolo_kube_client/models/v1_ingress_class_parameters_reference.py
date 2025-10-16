from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1IngressClassParametersReference",)


class V1IngressClassParametersReference(BaseModel):
    api_group: str | None = Field(None, alias="apiGroup")

    kind: str | None = Field(None, alias="kind")

    name: str | None = Field(None, alias="name")

    namespace: str | None = Field(None, alias="namespace")

    scope: str | None = Field(None, alias="scope")
