from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1TopologySelectorLabelRequirement",)


class V1TopologySelectorLabelRequirement(BaseModel):
    key: str | None = Field(default=None)

    values: list[str] = Field(default=[])
