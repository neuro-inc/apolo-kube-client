from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1NamespaceSpec",)


class V1NamespaceSpec(BaseModel):
    finalizers: list[str] = Field(default=[])
