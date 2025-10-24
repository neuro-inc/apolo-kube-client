from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1PodResourceClaim",)


class V1PodResourceClaim(BaseModel):
    """PodResourceClaim references exactly one ResourceClaim, either directly or by naming a ResourceClaimTemplate which is then turned into a ResourceClaim for the pod.

    It adds a name to it that uniquely identifies the ResourceClaim inside the Pod. Containers that need access to the ResourceClaim reference it with this name."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.PodResourceClaim"

    name: Annotated[
        str,
        Field(
            description="""Name uniquely identifies this resource claim inside the pod. This must be a DNS_LABEL."""
        ),
    ]

    resource_claim_name: Annotated[
        str | None,
        Field(
            alias="resourceClaimName",
            description="""ResourceClaimName is the name of a ResourceClaim object in the same namespace as this pod.

Exactly one of ResourceClaimName and ResourceClaimTemplateName must be set.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    resource_claim_template_name: Annotated[
        str | None,
        Field(
            alias="resourceClaimTemplateName",
            description="""ResourceClaimTemplateName is the name of a ResourceClaimTemplate object in the same namespace as this pod.

The template will be used to create a new ResourceClaim, which will be bound to this pod. When this pod is deleted, the ResourceClaim will also be deleted. The pod name and resource name, along with a generated component, will be used to form a unique name for the ResourceClaim, which will be recorded in pod.status.resourceClaimStatuses.

This field is immutable and no changes will be made to the corresponding ResourceClaim by the control plane after creating the ResourceClaim.

Exactly one of ResourceClaimName and ResourceClaimTemplateName must be set.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
