from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_certificate_signing_request_spec import V1CertificateSigningRequestSpec
from .v1_certificate_signing_request_status import V1CertificateSigningRequestStatus
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CertificateSigningRequest",)


class V1CertificateSigningRequest(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta(), exclude_if=_exclude_if)

    spec: Annotated[
        V1CertificateSigningRequestSpec,
        BeforeValidator(_default_if_none(V1CertificateSigningRequestSpec)),
    ] = Field(
        default_factory=lambda: V1CertificateSigningRequestSpec(),
        exclude_if=_exclude_if,
    )

    status: Annotated[
        V1CertificateSigningRequestStatus,
        BeforeValidator(_default_if_none(V1CertificateSigningRequestStatus)),
    ] = Field(
        default_factory=lambda: V1CertificateSigningRequestStatus(),
        exclude_if=_exclude_if,
    )
