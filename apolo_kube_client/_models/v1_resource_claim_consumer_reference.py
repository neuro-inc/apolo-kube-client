from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ResourceClaimConsumerReference",)


class V1ResourceClaimConsumerReference(BaseModel):
    """ResourceClaimConsumerReference contains enough information to let you locate the consumer of a ResourceClaim. The user must be a resource in the same namespace as the ResourceClaim."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1.ResourceClaimConsumerReference"
    )

    api_group: Annotated[
        str | None,
        Field(
            alias="apiGroup",
            description="""APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    name: Annotated[
        str, Field(description="""Name is the name of resource being referenced.""")
    ]

    resource: Annotated[
        str,
        Field(
            description="""Resource is the type of resource being referenced, for example "pods"."""
        ),
    ]

    uid: Annotated[
        str,
        Field(
            description="""UID identifies exactly one incarnation of the resource."""
        ),
    ]
