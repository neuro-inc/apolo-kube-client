from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_namespace_condition import V1NamespaceCondition

__all__ = ("V1NamespaceStatus",)


class V1NamespaceStatus(BaseModel):
    conditions: list[V1NamespaceCondition] | None = Field(None, alias="conditions")

    phase: str | None = Field(None, alias="phase")
