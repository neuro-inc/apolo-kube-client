from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ResourceClaimConsumerReference",)


class V1ResourceClaimConsumerReference(BaseModel):
    api_group: str | None = Field(
        default=None,
        serialization_alias="apiGroup",
        validation_alias=AliasChoices("api_group", "apiGroup"),
    )

    name: str | None = Field(default=None)

    resource: str | None = Field(default=None)

    uid: str | None = Field(default=None)
