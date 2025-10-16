from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1beta1ParentReference",)


class V1beta1ParentReference(BaseModel):
    group: str | None = Field(None, alias="group")

    name: str | None = Field(None, alias="name")

    namespace: str | None = Field(None, alias="namespace")

    resource: str | None = Field(None, alias="resource")
