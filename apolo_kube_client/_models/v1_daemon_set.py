from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
from .v1_daemon_set_spec import V1DaemonSetSpec
from .v1_daemon_set_status import V1DaemonSetStatus
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DaemonSet",)


class V1DaemonSet(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[
        V1DaemonSetSpec, BeforeValidator(_default_if_none(V1DaemonSetSpec))
    ] = Field(default_factory=lambda: V1DaemonSetSpec())

    status: Annotated[
        V1DaemonSetStatus, BeforeValidator(_default_if_none(V1DaemonSetStatus))
    ] = Field(default_factory=lambda: V1DaemonSetStatus())
