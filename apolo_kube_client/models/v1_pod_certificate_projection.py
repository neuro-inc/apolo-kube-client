from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1PodCertificateProjection",)


class V1PodCertificateProjection(BaseModel):
    certificate_chain_path: str | None = Field(
        default_factory=lambda: None, alias="certificateChainPath"
    )

    credential_bundle_path: str | None = Field(
        default_factory=lambda: None, alias="credentialBundlePath"
    )

    key_path: str | None = Field(default_factory=lambda: None, alias="keyPath")

    key_type: str | None = Field(default_factory=lambda: None, alias="keyType")

    max_expiration_seconds: int | None = Field(
        default_factory=lambda: None, alias="maxExpirationSeconds"
    )

    signer_name: str | None = Field(default_factory=lambda: None, alias="signerName")
