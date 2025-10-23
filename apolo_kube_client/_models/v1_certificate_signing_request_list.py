from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ListModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_certificate_signing_request import V1CertificateSigningRequest
from .v1_list_meta import V1ListMeta
from pydantic import BeforeValidator

__all__ = ("V1CertificateSigningRequestList",)


class V1CertificateSigningRequestList(ListModel):
    """CertificateSigningRequestList is a collection of CertificateSigningRequest objects"""

    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.certificates.v1.CertificateSigningRequestList"
    )

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="certificates.k8s.io", kind="CertificateSigningRequestList", version="v1"
    )

    api_version: Annotated[
        str | None,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    items: Annotated[
        list[V1CertificateSigningRequest],
        Field(
            description="""items is a collection of CertificateSigningRequest objects"""
        ),
    ]

    kind: Annotated[
        str | None,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    metadata: Annotated[
        V1ListMeta,
        Field(exclude_if=lambda v: v == V1ListMeta()),
        BeforeValidator(_default_if_none(V1ListMeta)),
    ] = V1ListMeta()
