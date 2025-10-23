from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_object_meta import V1ObjectMeta
from .v1beta1_resource_claim_spec import V1beta1ResourceClaimSpec
from .v1beta1_resource_claim_status import V1beta1ResourceClaimStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1ResourceClaim",)


class V1beta1ResourceClaim(ResourceModel):
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
        V1beta1ResourceClaimSpec,
        BeforeValidator(_default_if_none(V1beta1ResourceClaimSpec)),
    ] = Field(
        default_factory=lambda: V1beta1ResourceClaimSpec(), exclude_if=_exclude_if
    )

    status: Annotated[
        V1beta1ResourceClaimStatus,
        BeforeValidator(_default_if_none(V1beta1ResourceClaimStatus)),
    ] = Field(
        default_factory=lambda: V1beta1ResourceClaimStatus(), exclude_if=_exclude_if
    )
