from pydantic import BaseModel
from .utils import _collection_if_none
from .v1_certificate_signing_request_condition import (
    V1CertificateSigningRequestCondition,
)
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CertificateSigningRequestStatus",)


class V1CertificateSigningRequestStatus(BaseModel):
    certificate: str | None = None

    conditions: Annotated[
        list[V1CertificateSigningRequestCondition],
        BeforeValidator(_collection_if_none("[]")),
    ] = []
