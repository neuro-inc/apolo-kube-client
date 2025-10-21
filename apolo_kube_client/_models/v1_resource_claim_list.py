from pydantic import AliasChoices, Field
from .base import ListModel
from .base import _default_if_none
from .resource_v1_resource_claim import ResourceV1ResourceClaim
from .v1_list_meta import V1ListMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ResourceClaimList",)


class V1ResourceClaimList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[ResourceV1ResourceClaim] = []

    kind: str | None = None

    metadata: Annotated[V1ListMeta, BeforeValidator(_default_if_none(V1ListMeta))] = (
        Field(default_factory=lambda: V1ListMeta())
    )
