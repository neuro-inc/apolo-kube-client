from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_object_meta import V1ObjectMeta
from .v1_service_cidr_spec import V1ServiceCIDRSpec
from .v1_service_cidr_status import V1ServiceCIDRStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ServiceCIDR",)


class V1ServiceCIDR(ResourceModel):
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
        V1ServiceCIDRSpec, BeforeValidator(_default_if_none(V1ServiceCIDRSpec))
    ] = Field(default_factory=lambda: V1ServiceCIDRSpec(), exclude_if=_exclude_if)

    status: Annotated[
        V1ServiceCIDRStatus, BeforeValidator(_default_if_none(V1ServiceCIDRStatus))
    ] = Field(default_factory=lambda: V1ServiceCIDRStatus(), exclude_if=_exclude_if)
