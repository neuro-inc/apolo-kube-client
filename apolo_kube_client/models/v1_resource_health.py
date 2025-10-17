from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ResourceHealth",)


class V1ResourceHealth(BaseModel):
    health: str | None = Field(default=None)

    resource_id: str | None = Field(
        default=None,
        serialization_alias="resourceID",
        validation_alias=AliasChoices("resource_id", "resourceID"),
    )
