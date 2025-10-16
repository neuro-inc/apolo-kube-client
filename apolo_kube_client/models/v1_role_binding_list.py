from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1_role_binding import V1RoleBinding

__all__ = ("V1RoleBindingList",)


class V1RoleBindingList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1RoleBinding] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
