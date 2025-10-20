from pydantic import AliasChoices, Field
from .base import ListModel
from .v1_list_meta import V1ListMeta
from .v1_resource_quota import V1ResourceQuota

__all__ = ("V1ResourceQuotaList",)


class V1ResourceQuotaList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1ResourceQuota] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
