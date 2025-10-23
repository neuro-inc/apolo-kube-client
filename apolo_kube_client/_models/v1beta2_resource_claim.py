from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_object_meta import V1ObjectMeta
from .v1beta2_resource_claim_spec import V1beta2ResourceClaimSpec
from .v1beta2_resource_claim_status import V1beta2ResourceClaimStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta2ResourceClaim",)


class V1beta2ResourceClaim(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta(), exclude_if=_exclude_if)

    spec: Annotated[
        V1beta2ResourceClaimSpec,
        BeforeValidator(_default_if_none(V1beta2ResourceClaimSpec)),
    ] = Field(
        default_factory=lambda: V1beta2ResourceClaimSpec(), exclude_if=_exclude_if
    )

    status: Annotated[
        V1beta2ResourceClaimStatus,
        BeforeValidator(_default_if_none(V1beta2ResourceClaimStatus)),
    ] = Field(
        default_factory=lambda: V1beta2ResourceClaimStatus(), exclude_if=_exclude_if
    )
