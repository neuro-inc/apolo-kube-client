from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_container_extended_resource_request import V1ContainerExtendedResourceRequest

__all__ = ("V1PodExtendedResourceClaimStatus",)


class V1PodExtendedResourceClaimStatus(BaseModel):
    request_mappings: list[V1ContainerExtendedResourceRequest] = Field(
        default=[],
        serialization_alias="requestMappings",
        validation_alias=AliasChoices("request_mappings", "requestMappings"),
    )

    resource_claim_name: str | None = Field(
        default=None,
        serialization_alias="resourceClaimName",
        validation_alias=AliasChoices("resource_claim_name", "resourceClaimName"),
    )
