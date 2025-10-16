from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1alpha1ParamKind",)


class V1alpha1ParamKind(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")
