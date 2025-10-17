from pydantic import AliasChoices, BaseModel, Field
from .resource_v1_resource_claim import ResourceV1ResourceClaim
from .v1_list_meta import V1ListMeta

__all__ = ("V1ResourceClaimList",)


class V1ResourceClaimList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[ResourceV1ResourceClaim] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
