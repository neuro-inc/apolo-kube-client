from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1SuccessPolicyRule",)


class V1SuccessPolicyRule(BaseModel):
    succeeded_count: int | None = Field(None, alias="succeededCount")

    succeeded_indexes: str | None = Field(None, alias="succeededIndexes")
