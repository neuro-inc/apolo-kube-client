from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_container_extended_resource_request import V1ContainerExtendedResourceRequest

__all__ = ("V1PodExtendedResourceClaimStatus",)


class V1PodExtendedResourceClaimStatus(BaseModel):
    """PodExtendedResourceClaimStatus is stored in the PodStatus for the extended resource requests backed by DRA. It stores the generated name for the corresponding special ResourceClaim created by the scheduler."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.PodExtendedResourceClaimStatus"
    )

    request_mappings: Annotated[
        list[V1ContainerExtendedResourceRequest],
        Field(
            alias="requestMappings",
            description="""RequestMappings identifies the mapping of <container, extended resource backed by DRA> to  device request in the generated ResourceClaim.""",
        ),
    ]

    resource_claim_name: Annotated[
        str,
        Field(
            alias="resourceClaimName",
            description="""ResourceClaimName is the name of the ResourceClaim that was generated for the Pod in the namespace of the Pod.""",
        ),
    ]
