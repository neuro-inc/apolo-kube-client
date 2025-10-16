from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_certificate_signing_request import V1CertificateSigningRequest
from .v1_list_meta import V1ListMeta

__all__ = ("V1CertificateSigningRequestList",)


class V1CertificateSigningRequestList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1CertificateSigningRequest] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
