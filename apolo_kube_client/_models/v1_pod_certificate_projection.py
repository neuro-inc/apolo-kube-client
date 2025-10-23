from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1PodCertificateProjection",)


class V1PodCertificateProjection(BaseModel):
    certificate_chain_path: str | None = Field(
        default=None,
        serialization_alias="certificateChainPath",
        validation_alias=AliasChoices("certificate_chain_path", "certificateChainPath"),
        exclude_if=_exclude_if,
    )

    credential_bundle_path: str | None = Field(
        default=None,
        serialization_alias="credentialBundlePath",
        validation_alias=AliasChoices("credential_bundle_path", "credentialBundlePath"),
        exclude_if=_exclude_if,
    )

    key_path: str | None = Field(
        default=None,
        serialization_alias="keyPath",
        validation_alias=AliasChoices("key_path", "keyPath"),
        exclude_if=_exclude_if,
    )

    key_type: str | None = Field(
        default=None,
        serialization_alias="keyType",
        validation_alias=AliasChoices("key_type", "keyType"),
        exclude_if=_exclude_if,
    )

    max_expiration_seconds: int | None = Field(
        default=None,
        serialization_alias="maxExpirationSeconds",
        validation_alias=AliasChoices("max_expiration_seconds", "maxExpirationSeconds"),
        exclude_if=_exclude_if,
    )

    signer_name: str | None = Field(
        default=None,
        serialization_alias="signerName",
        validation_alias=AliasChoices("signer_name", "signerName"),
        exclude_if=_exclude_if,
    )
