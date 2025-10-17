from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1PodCertificateProjection",)


class V1PodCertificateProjection(BaseModel):
    certificate_chain_path: str | None = Field(
        default=None,
        serialization_alias="certificateChainPath",
        validation_alias=AliasChoices("certificate_chain_path", "certificateChainPath"),
    )

    credential_bundle_path: str | None = Field(
        default=None,
        serialization_alias="credentialBundlePath",
        validation_alias=AliasChoices("credential_bundle_path", "credentialBundlePath"),
    )

    key_path: str | None = Field(
        default=None,
        serialization_alias="keyPath",
        validation_alias=AliasChoices("key_path", "keyPath"),
    )

    key_type: str | None = Field(
        default=None,
        serialization_alias="keyType",
        validation_alias=AliasChoices("key_type", "keyType"),
    )

    max_expiration_seconds: int | None = Field(
        default=None,
        serialization_alias="maxExpirationSeconds",
        validation_alias=AliasChoices("max_expiration_seconds", "maxExpirationSeconds"),
    )

    signer_name: str | None = Field(
        default=None,
        serialization_alias="signerName",
        validation_alias=AliasChoices("signer_name", "signerName"),
    )
