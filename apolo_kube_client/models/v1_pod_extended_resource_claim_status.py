from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_container_extended_resource_request import V1ContainerExtendedResourceRequest

__all__ = ("V1PodExtendedResourceClaimStatus",)


class V1PodExtendedResourceClaimStatus(BaseModel):
    request_mappings: list[V1ContainerExtendedResourceRequest] = Field(
        default_factory=lambda: [], alias="requestMappings"
    )

    resource_claim_name: str | None = Field(
        default_factory=lambda: None, alias="resourceClaimName"
    )
