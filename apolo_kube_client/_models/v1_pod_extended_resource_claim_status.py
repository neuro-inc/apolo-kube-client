from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_container_extended_resource_request import V1ContainerExtendedResourceRequest
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PodExtendedResourceClaimStatus",)


class V1PodExtendedResourceClaimStatus(BaseModel):
    request_mappings: Annotated[
        list[V1ContainerExtendedResourceRequest],
        BeforeValidator(_collection_if_none("[]")),
    ] = Field(
        default=[],
        serialization_alias="requestMappings",
        validation_alias=AliasChoices("request_mappings", "requestMappings"),
        exclude_if=_exclude_if,
    )

    resource_claim_name: str | None = Field(
        default=None,
        serialization_alias="resourceClaimName",
        validation_alias=AliasChoices("resource_claim_name", "resourceClaimName"),
        exclude_if=_exclude_if,
    )
