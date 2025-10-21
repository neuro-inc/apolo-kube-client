from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CertificateSigningRequestSpec",)


class V1CertificateSigningRequestSpec(BaseModel):
    expiration_seconds: int | None = Field(
        default=None,
        serialization_alias="expirationSeconds",
        validation_alias=AliasChoices("expiration_seconds", "expirationSeconds"),
    )

    extra: Annotated[
        dict[str, list[str]], BeforeValidator(_collection_if_none("{}"))
    ] = {}

    groups: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    request: str | None = None

    signer_name: str | None = Field(
        default=None,
        serialization_alias="signerName",
        validation_alias=AliasChoices("signer_name", "signerName"),
    )

    uid: str | None = None

    usages: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    username: str | None = None
