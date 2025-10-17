from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1beta1_resource_claim_spec import V1beta1ResourceClaimSpec
from .v1beta1_resource_claim_status import V1beta1ResourceClaimStatus

__all__ = ("V1beta1ResourceClaim",)


class V1beta1ResourceClaim(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1beta1ResourceClaimSpec = Field(
        default_factory=lambda: V1beta1ResourceClaimSpec()
    )

    status: V1beta1ResourceClaimStatus = Field(
        default_factory=lambda: V1beta1ResourceClaimStatus()
    )
