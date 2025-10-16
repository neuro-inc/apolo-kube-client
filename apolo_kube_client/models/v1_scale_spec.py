from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1ScaleSpec",)


class V1ScaleSpec(BaseModel):
    replicas: int | None = Field(None, alias="replicas")
