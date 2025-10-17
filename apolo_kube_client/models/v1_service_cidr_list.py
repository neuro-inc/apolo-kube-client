from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_service_cidr import V1ServiceCIDR

__all__ = ("V1ServiceCIDRList",)


class V1ServiceCIDRList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1ServiceCIDR] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
