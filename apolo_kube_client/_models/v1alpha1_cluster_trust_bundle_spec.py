from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1alpha1ClusterTrustBundleSpec",)


class V1alpha1ClusterTrustBundleSpec(BaseModel):
    signer_name: str | None = Field(
        default=None,
        serialization_alias="signerName",
        validation_alias=AliasChoices("signer_name", "signerName"),
        exclude_if=_exclude_if,
    )

    trust_bundle: str | None = Field(
        default=None,
        serialization_alias="trustBundle",
        validation_alias=AliasChoices("trust_bundle", "trustBundle"),
        exclude_if=_exclude_if,
    )
