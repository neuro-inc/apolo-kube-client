from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_certificate_signing_request import V1CertificateSigningRequest
from .v1_list_meta import V1ListMeta

__all__ = ("V1CertificateSigningRequestList",)


class V1CertificateSigningRequestList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1CertificateSigningRequest] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
