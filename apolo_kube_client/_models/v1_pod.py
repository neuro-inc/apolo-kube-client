from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
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
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[V1PodSpec, BeforeValidator(_default_if_none(V1PodSpec))] = Field(
        default_factory=lambda: V1PodSpec()
    )

    status: Annotated[V1PodStatus, BeforeValidator(_default_if_none(V1PodStatus))] = (
        Field(default_factory=lambda: V1PodStatus())
    )
