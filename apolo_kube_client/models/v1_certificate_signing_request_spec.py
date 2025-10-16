from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1CertificateSigningRequestSpec",)


class V1CertificateSigningRequestSpec(BaseModel):
    expiration_seconds: int | None = Field(None, alias="expirationSeconds")

    extra: dict[str, list[str]] | None = Field(None, alias="extra")

    groups: list[str] | None = Field(None, alias="groups")

    request: str | None = Field(None, alias="request")

    signer_name: str | None = Field(None, alias="signerName")

    uid: str | None = Field(None, alias="uid")

    usages: list[str] | None = Field(None, alias="usages")

    username: str | None = Field(None, alias="username")
