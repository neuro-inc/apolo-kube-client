from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1ScaleStatus",)


class V1ScaleStatus(BaseModel):
    replicas: int | None = Field(None, alias="replicas")

    selector: str | None = Field(None, alias="selector")
