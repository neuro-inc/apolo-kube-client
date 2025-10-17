from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1IPBlock",)


class V1IPBlock(BaseModel):
    cidr: str | None = Field(default_factory=lambda: None)

    except_: list[str] = Field(default_factory=lambda: [], alias="except")
