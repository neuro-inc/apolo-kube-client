from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ListMeta",)


class V1ListMeta(BaseModel):
    continue_: str | None = Field(default_factory=lambda: None, alias="continue")

    remaining_item_count: int | None = Field(
        default_factory=lambda: None, alias="remainingItemCount"
    )

    resource_version: str | None = Field(
        default_factory=lambda: None, alias="resourceVersion"
    )

    self_link: str | None = Field(default_factory=lambda: None, alias="selfLink")
