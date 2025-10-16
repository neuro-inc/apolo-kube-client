from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1OwnerReference",)


class V1OwnerReference(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    block_owner_deletion: bool | None = Field(None, alias="blockOwnerDeletion")

    controller: bool | None = Field(None, alias="controller")

    kind: str | None = Field(None, alias="kind")

    name: str | None = Field(None, alias="name")

    uid: str | None = Field(None, alias="uid")
