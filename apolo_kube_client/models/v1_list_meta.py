from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1ListMeta",)


class V1ListMeta(BaseModel):
    _continue: str | None = Field(None, alias="continue")

    remaining_item_count: int | None = Field(None, alias="remainingItemCount")

    resource_version: str | None = Field(None, alias="resourceVersion")

    self_link: str | None = Field(None, alias="selfLink")
