from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1CertificateSigningRequestSpec",)


class V1CertificateSigningRequestSpec(BaseModel):
    expiration_seconds: int | None = Field(
        default_factory=lambda: None, alias="expirationSeconds"
    )

    extra: dict[str, list[str]] = Field(default_factory=lambda: {}, alias="extra")

    groups: list[str] = Field(default_factory=lambda: [], alias="groups")

    request: str | None = Field(default_factory=lambda: None, alias="request")

    signer_name: str | None = Field(default_factory=lambda: None, alias="signerName")

    uid: str | None = Field(default_factory=lambda: None, alias="uid")

    usages: list[str] = Field(default_factory=lambda: [], alias="usages")

    username: str | None = Field(default_factory=lambda: None, alias="username")
