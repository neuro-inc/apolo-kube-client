from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_object_meta import V1ObjectMeta
from .v1_pod_spec import V1PodSpec
from .v1_pod_status import V1PodStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Pod",)


class V1Pod(ResourceModel):
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

    spec: Annotated[V1PodSpec, BeforeValidator(_default_if_none(V1PodSpec))] = Field(
        default_factory=lambda: V1PodSpec(), exclude_if=_exclude_if
    )

    status: Annotated[V1PodStatus, BeforeValidator(_default_if_none(V1PodStatus))] = (
        Field(default_factory=lambda: V1PodStatus(), exclude_if=_exclude_if)
    )
