from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1StatefulSetOrdinals",)


class V1StatefulSetOrdinals(BaseModel):
    start: int | None = Field(default_factory=lambda: None)
