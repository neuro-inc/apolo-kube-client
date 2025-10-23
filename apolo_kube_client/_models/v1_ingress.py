from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_ingress_spec import V1IngressSpec
from .v1_ingress_status import V1IngressStatus
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Ingress",)


class V1Ingress(ResourceModel):
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

    spec: Annotated[V1IngressSpec, BeforeValidator(_default_if_none(V1IngressSpec))] = (
        Field(default_factory=lambda: V1IngressSpec(), exclude_if=_exclude_if)
    )

    status: Annotated[
        V1IngressStatus, BeforeValidator(_default_if_none(V1IngressStatus))
    ] = Field(default_factory=lambda: V1IngressStatus(), exclude_if=_exclude_if)
