from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1IPBlock",)


class V1IPBlock(BaseModel):
    cidr: str | None = Field(None, alias="cidr")

    _except: list[str] | None = Field(None, alias="except")
