from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ListMeta",)


class V1ListMeta(BaseModel):
    continue_: str | None = Field(
        default=None,
        serialization_alias="continue",
        validation_alias=AliasChoices("continue_", "continue"),
    )

    remaining_item_count: int | None = Field(
        default=None,
        serialization_alias="remainingItemCount",
        validation_alias=AliasChoices("remaining_item_count", "remainingItemCount"),
    )

    resource_version: str | None = Field(
        default=None,
        serialization_alias="resourceVersion",
        validation_alias=AliasChoices("resource_version", "resourceVersion"),
    )

    self_link: str | None = Field(
        default=None,
        serialization_alias="selfLink",
        validation_alias=AliasChoices("self_link", "selfLink"),
    )
