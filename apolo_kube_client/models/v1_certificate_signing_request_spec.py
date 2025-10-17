from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1CertificateSigningRequestSpec",)


class V1CertificateSigningRequestSpec(BaseModel):
    expiration_seconds: int | None = Field(
        default=None,
        serialization_alias="expirationSeconds",
        validation_alias=AliasChoices("expiration_seconds", "expirationSeconds"),
    )

    extra: dict[str, list[str]] = Field(default={})

    groups: list[str] = Field(default=[])

    request: str | None = Field(default=None)

    signer_name: str | None = Field(
        default=None,
        serialization_alias="signerName",
        validation_alias=AliasChoices("signer_name", "signerName"),
    )

    uid: str | None = Field(default=None)

    usages: list[str] = Field(default=[])

    username: str | None = Field(default=None)
