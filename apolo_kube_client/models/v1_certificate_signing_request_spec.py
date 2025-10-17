from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1CertificateSigningRequestSpec",)


class V1CertificateSigningRequestSpec(BaseModel):
    expiration_seconds: int | None = Field(
        default=None,
        serialization_alias="expirationSeconds",
        validation_alias=AliasChoices("expiration_seconds", "expirationSeconds"),
    )

    extra: dict[str, list[str]] = {}

    groups: list[str] = []

    request: str | None = None

    signer_name: str | None = Field(
        default=None,
        serialization_alias="signerName",
        validation_alias=AliasChoices("signer_name", "signerName"),
    )

    uid: str | None = None

    usages: list[str] = []

    username: str | None = None
