from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1beta2ResourceClaimConsumerReference",)


class V1beta2ResourceClaimConsumerReference(BaseModel):
    api_group: str | None = Field(default_factory=lambda: None, alias="apiGroup")

    name: str | None = Field(default_factory=lambda: None)

    resource: str | None = Field(default_factory=lambda: None)

    uid: str | None = Field(default_factory=lambda: None)
