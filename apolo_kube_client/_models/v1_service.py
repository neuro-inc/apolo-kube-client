from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_object_meta import V1ObjectMeta
from .v1_service_spec import V1ServiceSpec
from .v1_service_status import V1ServiceStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Service",)


class V1Service(ResourceModel):
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

    spec: Annotated[V1ServiceSpec, BeforeValidator(_default_if_none(V1ServiceSpec))] = (
        Field(default_factory=lambda: V1ServiceSpec(), exclude_if=_exclude_if)
    )

    status: Annotated[
        V1ServiceStatus, BeforeValidator(_default_if_none(V1ServiceStatus))
    ] = Field(default_factory=lambda: V1ServiceStatus(), exclude_if=_exclude_if)
