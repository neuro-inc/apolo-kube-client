from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_certificate_signing_request_condition import (
    V1CertificateSigningRequestCondition,
)
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CertificateSigningRequestStatus",)


class V1CertificateSigningRequestStatus(BaseModel):
    certificate: str | None = Field(default=None, exclude_if=_exclude_if)

    conditions: Annotated[
        list[V1CertificateSigningRequestCondition],
        BeforeValidator(_collection_if_none("[]")),
    ] = Field(default=[], exclude_if=_exclude_if)
