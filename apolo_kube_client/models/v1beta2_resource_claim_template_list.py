from pydantic import AliasChoices, Field
from .base import ListModel
from .v1_list_meta import V1ListMeta
from .v1beta2_resource_claim_template import V1beta2ResourceClaimTemplate

__all__ = ("V1beta2ResourceClaimTemplateList",)


class V1beta2ResourceClaimTemplateList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1beta2ResourceClaimTemplate] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
