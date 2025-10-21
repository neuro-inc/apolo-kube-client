from pydantic import AliasChoices, Field
from .base import ListModel
from .base import _default_if_none
from .v1_list_meta import V1ListMeta
from .v1alpha1_pod_certificate_request import V1alpha1PodCertificateRequest
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1alpha1PodCertificateRequestList",)


class V1alpha1PodCertificateRequestList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1alpha1PodCertificateRequest] = []

    kind: str | None = None

    metadata: Annotated[V1ListMeta, BeforeValidator(_default_if_none(V1ListMeta))] = (
        Field(default_factory=lambda: V1ListMeta())
    )
