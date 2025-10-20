from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1beta1ClusterTrustBundleSpec",)


class V1beta1ClusterTrustBundleSpec(BaseModel):
    signer_name: str | None = Field(
        default=None,
        serialization_alias="signerName",
        validation_alias=AliasChoices("signer_name", "signerName"),
    )

    trust_bundle: str | None = Field(
        default=None,
        serialization_alias="trustBundle",
        validation_alias=AliasChoices("trust_bundle", "trustBundle"),
    )
