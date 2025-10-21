from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_resource_claim_spec import V1ResourceClaimSpec
from .v1_resource_claim_status import V1ResourceClaimStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("ResourceV1ResourceClaim",)


class ResourceV1ResourceClaim(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[
        V1ResourceClaimSpec, BeforeValidator(_default_if_none(V1ResourceClaimSpec))
    ] = Field(default_factory=lambda: V1ResourceClaimSpec())

    status: Annotated[
        V1ResourceClaimStatus, BeforeValidator(_default_if_none(V1ResourceClaimStatus))
    ] = Field(default_factory=lambda: V1ResourceClaimStatus())
