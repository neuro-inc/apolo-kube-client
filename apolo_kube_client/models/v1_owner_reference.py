from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1OwnerReference",)


class V1OwnerReference(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    block_owner_deletion: bool | None = Field(
        default_factory=lambda: None, alias="blockOwnerDeletion"
    )

    controller: bool | None = Field(default_factory=lambda: None)

    kind: str | None = Field(default_factory=lambda: None)

    name: str | None = Field(default_factory=lambda: None)

    uid: str | None = Field(default_factory=lambda: None)
