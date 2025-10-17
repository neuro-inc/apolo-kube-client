from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1beta2_resource_claim import V1beta2ResourceClaim

__all__ = ("V1beta2ResourceClaimList",)


class V1beta2ResourceClaimList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1beta2ResourceClaim] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
