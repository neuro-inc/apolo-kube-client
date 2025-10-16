from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1Capabilities",)


class V1Capabilities(BaseModel):
    add: list[str] | None = Field(None, alias="add")

    drop: list[str] | None = Field(None, alias="drop")
