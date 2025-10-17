from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_network_policy import V1NetworkPolicy

__all__ = ("V1NetworkPolicyList",)


class V1NetworkPolicyList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1NetworkPolicy] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
