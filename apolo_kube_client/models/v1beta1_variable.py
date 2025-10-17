from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1beta1Variable",)


class V1beta1Variable(BaseModel):
    expression: str | None = Field(default=None)

    name: str | None = Field(default=None)
